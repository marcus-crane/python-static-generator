import os
import tempfile

from test import utils


def test_load_fixture():
    tempdir = tempfile.TemporaryDirectory()
    tempfile.mkdtemp(dir=f"{tempdir}/fixtures")

    os.mkdir()
    actual = utils.load_fixture(file, path)
    tempdir.close()