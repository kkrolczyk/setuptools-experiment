import os
import sys

THIS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(THIS_DIR, os.pardir))
# tests are not a package, need to be able to find project pkg
import pkg_directory  # noqa: E402


def test_should_pass():
    print(pkg_directory)
    assert True  # noqa: S101
