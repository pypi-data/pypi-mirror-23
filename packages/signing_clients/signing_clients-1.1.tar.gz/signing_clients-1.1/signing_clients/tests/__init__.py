# coding=utf-8
# ***** BEGIN LICENSE BLOCK *****
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
# ***** END LICENSE BLOCK *****

import os.path
import shutil
import tempfile
import unittest

from hashlib import sha1

from signing_clients.apps import (
    force_bytes,
    Manifest,
    JarExtractor,
    ParsingError,
    ZipFile,
    file_key,
    get_signature_serial_number,
    ignore_certain_metainf_files
)


MANIFEST_BODY = b"""Name: test-file
Digest-Algorithms: MD5 SHA1
MD5-Digest: 5BXJnAbD0DzWPCj6Ve/16w==
SHA1-Digest: 5Hwcbg1KaPMqjDAXV/XDq/f30U0=

Name: test-dir/nested-test-file
Digest-Algorithms: MD5 SHA1
MD5-Digest: 53dwfEn/GnFiWp0NQyqWlA==
SHA1-Digest: 4QzlrC8QyhQW1T0/Nay5kRr3gVo=
"""

MANIFEST = b"Manifest-Version: 1.0\n\n" + MANIFEST_BODY

SIGNATURE = b"""Signature-Version: 1.0
MD5-Digest-Manifest: dughN2Z8uP3eXIZm7GVpjA==
SHA1-Digest-Manifest: rnDwKcEuRYqy57DFyzwK/Luul+0=
"""

SIGNATURES_BODY = b"""Name: test-file
Digest-Algorithms: MD5 SHA1
MD5-Digest: jf86A0RSFH3oREWLkRAoIg==
SHA1-Digest: 9O+Do4sVlAh82x9ZYu1GbtyNToA=

Name: test-dir/nested-test-file
Digest-Algorithms: MD5 SHA1
MD5-Digest: YHTqD4SINsoZngWvbGIhAA==
SHA1-Digest: lys436ZGYKrHY6n57Iy/EyF5FuI=
"""

SIGNATURES = SIGNATURE + b"\n" + SIGNATURES_BODY

EXTRA_NEWLINE_SIGNATURE = b"""Signature-Version: 1.0
MD5-Digest-Manifest: A3IkNTcP2L6JzwQzkp+6Kg==
SHA1-Digest-Manifest: xQKf9C1JcIjfZoFxTWt3pzW2KYI=

"""

EXTRA_NEWLINE_SIGNATURES = EXTRA_NEWLINE_SIGNATURE + b"\n" + SIGNATURES_BODY + b"\n"  # noqa

CONTINUED_MANIFEST = MANIFEST + b"""
Name: test-dir/nested-test-dir/nested-test-dir/nested-test-dir/nested-te
 st-file
Digest-Algorithms: MD5 SHA1
MD5-Digest: 53dwfEn/GnFiWp0NQyqWlA==
SHA1-Digest: 4QzlrC8QyhQW1T0/Nay5kRr3gVo=
"""

# Test for 72 byte limit test
BROKEN_MANIFEST = MANIFEST + b"""
Name: test-dir/nested-test-dir/nested-test-dir/nested-test-dir/nested-test-file
Digest-Algorithms: MD5 SHA1
MD5-Digest: 53dwfEn/GnFiWp0NQyqWlA==
SHA1-Digest: 4QzlrC8QyhQW1T0/Nay5kRr3gVo=
"""

VERY_LONG_MANIFEST = b"""Manifest-Version: 1.0

Name: test-file
Digest-Algorithms: MD5 SHA1
MD5-Digest: 5BXJnAbD0DzWPCj6Ve/16w==
SHA1-Digest: 5Hwcbg1KaPMqjDAXV/XDq/f30U0=

Name: test-dir/nested-test-file
Digest-Algorithms: MD5 SHA1
MD5-Digest: 53dwfEn/GnFiWp0NQyqWlA==
SHA1-Digest: 4QzlrC8QyhQW1T0/Nay5kRr3gVo=

Name: test-dir/nested-test-dir-0/nested-test-dir-1/nested-test-dir-2/lon
 g-path-name-test
Digest-Algorithms: MD5 SHA1
MD5-Digest: 9bU/UEp83EbO/DWN3Ds/cg==
SHA1-Digest: lIbbwE8/2LFOD00+bJ/Wu80lR/I=
"""

# Test for Unicode
UNICODE_MANIFEST = u"""Manifest-Version: 1.0

Name: test-dir/súité-höñe.txt
Digest-Algorithms: MD5 SHA1
MD5-Digest: +ZqzWWcMtOrWxs8Xr/tt+A==
SHA1-Digest: B5HkCxgt6fXNr+dWPwXH2aALVWk=
"""


def get_file(fname):
    return os.path.join(os.path.dirname(__file__), fname)


class SigningTest(unittest.TestCase):

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix='tmp-signing-clients-test-')
        self.addCleanup(lambda: shutil.rmtree(self.tmpdir))

    def tmp_file(self, fname):
        return os.path.join(self.tmpdir, fname)

    def _extract(self, omit=False, newlines=False):
        return JarExtractor(get_file('test-jar.zip'),
                            omit_signature_sections=omit,
                            extra_newlines=newlines)

    def test_00_extractor(self):
        self.assertTrue(isinstance(self._extract(), JarExtractor))

    def test_01_manifest(self):
        extracted = self._extract()
        self.assertEqual(force_bytes(extracted.manifest), MANIFEST)
        extracted = self._extract(newlines=True)
        self.assertEqual(force_bytes(extracted.manifest), MANIFEST + b"\n")

    def test_02_signature(self):
        extracted = self._extract()
        self.assertEqual(force_bytes(extracted.signature), SIGNATURE)
        extracted = self._extract(newlines=True)
        self.assertEqual(force_bytes(extracted.signature), EXTRA_NEWLINE_SIGNATURE)

    def test_03_signatures(self):
        extracted = self._extract()
        self.assertEqual(force_bytes(extracted.signatures), SIGNATURES)
        extracted = self._extract(newlines=True)
        self.assertEqual(force_bytes(extracted.signatures), EXTRA_NEWLINE_SIGNATURES)

    def test_04_signatures_omit(self):
        extracted = self._extract(True)
        self.assertEqual(force_bytes(extracted.signatures), SIGNATURE)

    def test_05_continuation(self):
        manifest = Manifest.parse(CONTINUED_MANIFEST)
        self.assertEqual(force_bytes(manifest), CONTINUED_MANIFEST)

    def test_06_line_too_long(self):
        self.assertRaises(ParsingError, Manifest.parse, BROKEN_MANIFEST)

    def test_07_wrapping(self):
        extracted = JarExtractor(get_file('test-jar-long-path.zip'),
                                 omit_signature_sections=False)
        self.assertEqual(force_bytes(extracted.manifest), VERY_LONG_MANIFEST)

    def test_08_unicode(self):
        extracted = JarExtractor(get_file('test-jar-unicode.zip'),
                                 omit_signature_sections=False)
        self.assertEqual(
            force_bytes(extracted.manifest).decode('utf-8'), UNICODE_MANIFEST)

    def test_09_serial_number_extraction(self):
        with open(get_file('zigbert.test.pkcs7.der'), 'rb') as f:
            serialno = get_signature_serial_number(f.read())
        # Signature occured on Thursday, January 22nd 2015 at 11:02:22am PST
        # The signing service returns a Python time.time() value multiplied
        # by 1000 to get a (hopefully) truly unique serial number
        self.assertEqual(1421953342960, serialno)

    def test_10_resigning_manifest_exclusions(self):
        # This zip contains META-INF/manifest.mf, META-INF/zigbert.sf, and
        # META-INF/zigbert.rsa in addition to the contents of the basic test
        # archive test-jar.zip
        extracted = JarExtractor(get_file('test-jar-meta-inf-exclude.zip'),
                                 omit_signature_sections=True)
        self.assertEqual(force_bytes(extracted.manifest), MANIFEST)

    def test_11_make_signed(self):
        extracted = JarExtractor(get_file('test-jar.zip'),
                                 omit_signature_sections=True)
        # Not a valid signature but a PKCS7 data blob, at least
        with open(get_file('zigbert.test.pkcs7.der'), 'rb') as f:
            signature = f.read()
            signature_digest = sha1()
            signature_digest.update(signature)

        signed_file = self.tmp_file('test-jar-signed.zip')
        sigpath = 'zoidberg'
        extracted.make_signed(signature, signed_file, sigpath=sigpath)
        # Now verify the signed zipfile's contents
        with ZipFile(signed_file, 'r') as zin:
            # sorted(...) should result in the following order:
            files = ['test-file', 'META-INF/manifest.mf',
                     'META-INF/zoidberg.rsa',
                     'META-INF/zoidberg.sf',
                     'test-dir/', 'test-dir/nested-test-file']
            zfiles = [f.filename for f in sorted(zin.filelist, key=file_key)]
            self.assertEqual(files, zfiles)
            zip_sig_digest = sha1()
            zip_sig_digest.update(zin.read('META-INF/zoidberg.rsa'))

            self.assertEqual(signature_digest.hexdigest(),
                             zip_sig_digest.hexdigest())
        # And make sure the manifest is correct
        signed = JarExtractor(signed_file, omit_signature_sections=True)
        self.assertEqual(force_bytes(extracted.manifest), force_bytes(signed.manifest))

    def test_11_make_signed_default_sigpath(self):
        extracted = JarExtractor(get_file('test-jar.zip'),
                                 omit_signature_sections=True)
        # Not a valid signature but a PKCS7 data blob, at least
        with open(get_file('zigbert.test.pkcs7.der'), 'rb') as f:
            signature = f.read()
            signature_digest = sha1()
            signature_digest.update(signature)

        signed_file = self.tmp_file('test-jar-signed.zip')
        extracted.make_signed(signature, signed_file)

        with ZipFile(signed_file, 'r') as zin:
            files = ['test-file', 'META-INF/manifest.mf',
                     'META-INF/zigbert.rsa',
                     'META-INF/zigbert.sf',
                     'test-dir/', 'test-dir/nested-test-file']
            zfiles = [f.filename for f in sorted(zin.filelist, key=file_key)]
            self.assertEqual(files, zfiles)
            zip_sig_digest = sha1()
            zip_sig_digest.update(zin.read('META-INF/zigbert.rsa'))

            self.assertEqual(signature_digest.hexdigest(),
                             zip_sig_digest.hexdigest())

        signed = JarExtractor(signed_file, omit_signature_sections=True)
        self.assertEqual(force_bytes(extracted.manifest), force_bytes(signed.manifest))

    # See https://bugzil.la/1169574
    def test_12_metainf_case_sensitivity(self):
        self.assertTrue(ignore_certain_metainf_files('meta-inf/manifest.mf'))
        self.assertTrue(ignore_certain_metainf_files('MeTa-InF/MaNiFeSt.Mf'))
        self.assertFalse(ignore_certain_metainf_files('meta-inf/pickles.mf'))

