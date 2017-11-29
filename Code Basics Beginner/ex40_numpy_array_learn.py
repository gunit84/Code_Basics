#!python3

"""Numpy Learning... """

__author__ = "Gavin Jones"

import numpy as np

# 2 dimensional numpy array
twoDimensions = np.array([[1, 2], [3, 4]])

# get the list of dimensions
print(twoDimensions.ndim)

# get the bytesize of these elements
print(twoDimensions.itemsize)

# decimal type
print(twoDimensions.dtype)

# size the total amount of elements
print(twoDimensions.size)

# shape represents the amount of rows and columns
print(twoDimensions.shape)

# initialise a number with all zeros 3 columns with 4 rows
print(np.zeros((3, 4)))

# initialise a number with all ones 3 columns with 4 rows
print(np.ones((3, 4)))

# create a numpy array range
print(np.arange(1, 5))

# numpy linspace
print(np.linspace(1, 5, 10))

# reshape the array's row and columns
print(twoDimensions.reshape(1, 4))

# flatten the array make it one dimensional
print(twoDimensions.ravel())

# print the minimum
print(twoDimensions.min())

# print the maximum
print(twoDimensions.max())

# sum the numbers
print(twoDimensions.sum())

# sum the numbers in the first column
print(twoDimensions.sum(axis=0))

# sum the numbers in the rows
print(twoDimensions.sum(axis=1))

# square root with numpy
print(np.sqrt((twoDimensions)))

# standard deviatiop
print(np.std(twoDimensions))

# also has the ability to math, multiplication on arrays


