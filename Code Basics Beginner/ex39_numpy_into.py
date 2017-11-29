#!python3

"""Learning Numpy... ADD 2 LISTS of numbers using python list and then numpy array and compare them """

__author__ = "Gavin Jones"

import time

import numpy as np

SIZE = 1000000

# 2 standard Python Lists
l1 = range(SIZE)
l2 = range(SIZE)

# 2 standard numpy arrays
a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# timing the addition of the lists
start = time.time()
# list comprehension needed...
result = [(x + y) for x, y in zip(l1, l2)]
print("Python list took", (time.time() - start) * 1000)

# timing the addition of the arrays
start = time.time()
result = a1 + a2
print("numpy array took", (time.time() - start) * 1000)
