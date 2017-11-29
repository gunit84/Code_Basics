#!python3

"""Learning Numpy... """

__author__ = "Gavin Jones"

import sys

import numpy as np

testList = range(1000)

# get the size in memory in bytes of the std range function
print(sys.getsizeof(5) * len(testList))

# get the size in memory in bytes of the numpy arange functon
array = np.arange(1000)
print(array.size * array.itemsize)

