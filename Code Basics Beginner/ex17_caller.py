#!python3

"""Caller Function Importing the Module... """

__author__ = "Gavin Jones"

import sys

import ex17_if_main

# Appends the system PATH to use this local Folder Path
sys.path.append("")

print("I am in ex17_caller.py")

ex17_if_main.calculate_area(5, 10)
