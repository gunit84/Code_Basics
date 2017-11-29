#!python3

"""Python Testing... File to test file ex34_pytest_mathlib """

__author__ = "Gavin Jones"

import sys
import pytest

import ex34_pytest_mathlib

# Needed to import the module ex34_pytest_mathlib from the relative directory.
sys.path.append("")


# Functions to use for Testing...
@pytest.mark.skipif(sys.version_info > (3, 5), reason="I don't want to run this test.")
def test_calc_total():
    total = ex34_pytest_mathlib.calc_total(4, 5)
    assert total == 9


def test_calc_multiply():
    total = ex34_pytest_mathlib.calc_multiply(4, 5)
    assert total == 20
