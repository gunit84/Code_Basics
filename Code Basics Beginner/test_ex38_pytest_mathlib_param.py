#!python3

"""Python Testing... File to test file ex34_pytest_mathlib """

__author__ = "Gavin Jones"

import sys

import pytest

import ex38_pytest_mathlib

# Needed to import the module ex34_pytest_mathlib from the relative directory.
sys.path.append("")


# Functions to use for Testing...
@pytest.mark.paremetrize("test_input, expected_output",
                         [
                             (5, 25),
                             (9, 81),
                             (10, 100)
                         ]
                         )
def test_calc_square(test_input, expected_output):
    result = ex38_pytest_mathlib.calc_square(test_input)
    assert result == expected_output
