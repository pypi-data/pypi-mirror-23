#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `sign_xpi_lib` package."""

import os.path
import pytest
import tempfile
from zipfile import ZipFile

from sign_xpi_lib import XPIFile


TEST_DIR, _ = os.path.split(__file__)


def get_test_file(filename):
    return os.path.join(TEST_DIR, filename)


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_xpi_signer_manifest_seems_sane():
    """Verify that an XPI file's manifest is accessible and has stuff in it."""
    x = XPIFile(get_test_file('hypothetical-addon-unsigned.xpi'))
    assert str(x.manifest) == """Manifest-Version: 1.0

Name: content.js
Digest-Algorithms: MD5 SHA1 SHA256
MD5-Digest: 1USWi3/aQcBJdik7zRPi3Q==
SHA1-Digest: hStL5xaG/NV6z3PrVqBn7pA/ovY=
SHA256-Digest: SyzN6k1xO7bMtWm4F0qmd9BQNII0Pdj9qAYt+31kwQ8=

Name: manifest.json
Digest-Algorithms: MD5 SHA1 SHA256
MD5-Digest: XDjUvCuM+uVn3WZ0On8GZA==
SHA1-Digest: YD+s4lbJBrPCsTjlppad7kG/f8Y=
SHA256-Digest: UgduoifBgZBYEpRuuo5PTYAGSqffIIc0Q71NLWiIObc=

Name: README.txt
Digest-Algorithms: MD5 SHA1 SHA256
MD5-Digest: X/eti4SGeMla30jsgvXsYg==
SHA1-Digest: eYJ+zdu1ufrA0ZNH82aj17iQ23U=
SHA256-Digest: qf/cDvSBp+jx5x7/QUVNZSex+WuSOr9bQ3acXEKXc6o=

Name: 悶絶ñé💩ı
Digest-Algorithms: MD5 SHA1 SHA256
MD5-Digest: 1B2M2Y8AsgTpgAmY7PhCfg==
SHA1-Digest: 2jmj7l5rSw0yVb/vlWAYkK/YBwk=
SHA256-Digest: 47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=

Name: icons/hypothetical-48.png
Digest-Algorithms: MD5 SHA1 SHA256
MD5-Digest: NyKobXm4DOyAkCDBomN2NA==
SHA1-Digest: kOANs5plfc23hWQnOPTtGBGhj/I=
SHA256-Digest: hho3C/YNs59bdqjBl6JpcBtA5I4paeBb8wG/Dr7nUM4=

"""


def test_xpi_signer_signature_seems_sane():
    """Verify that an XPI file's manifest is accessible and has stuff in it."""
    x = XPIFile(get_test_file('hypothetical-addon-unsigned.xpi'))

    assert x.signature == """Signature-Version: 1.0
MD5-Digest-Manifest: 5zaRZmvOY+2TpuvBZMYgwg==
SHA1-Digest-Manifest: kcG3SrNMA4bTbBDA6iOx5t93wqw=
SHA256-Digest-Manifest: j3T7lorOa6BjdPFdCWD5bEvDDrZQmR48zzBuuJx9CkQ=

"""


def test_xpi_signer_make_signed_seems_sane():
    x = XPIFile(get_test_file('hypothetical-addon-unsigned.xpi'))
    signed_name = 'hypothetical-addon-signed.xpi'
    signature = b'This signature is valid'
    signed_manifest = b'Signature-Version: 1.0-test'
    with tempfile.TemporaryDirectory() as sandbox:
        signed_file = os.path.join(sandbox, signed_name)
        x.make_signed(signed_file,
                      'mozilla.rsa',
                      signed_manifest, signature)

        z = ZipFile(signed_file, 'r')
        infolist = z.infolist()
        assert infolist[0].filename == 'META-INF/mozilla.rsa'
        assert signature == z.read('META-INF/mozilla.rsa')
        assert signed_manifest == z.read('META-INF/mozilla.sf')


def test_xpi_signer_doesnt_overwrite_files():
    x = XPIFile(get_test_file('hypothetical-addon-unsigned.xpi'))
    signed_name = 'hypothetical-addon-signed.xpi'
    signature = b'This signature is valid'
    signed_manifest = b'Signature-Version: 1.0-test'
    with tempfile.TemporaryDirectory() as sandbox:
        signed_file = os.path.join(sandbox, signed_name)
        open(signed_file, 'w').write('I already exist')

        with pytest.raises(FileExistsError):
            x.make_signed(signed_file,
                          'mozilla.rsa',
                          signed_manifest, signature)
