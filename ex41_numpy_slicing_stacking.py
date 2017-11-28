#!python3

"""Python 3 numpy slicing and stacking with boolean arrays numpy """

__author__ = "Gavin Jones"

import numpy as np

# numpy array example splicing
a = np.array([[6, 7, 8],
              [1, 2, 3],
              [9, 3, 2]])

print(a[0:2])

# like range steps over rows 0, 1 and it's printing the second elements in the row
print(a[0:2, 2])

# prints the last row
print(a[-1])

# remember row, column, element
print(a[-1, 0:2])

# print middle columns: first is all the rows :, second is rows 1-2
print(a[:, 1:3])

# iterate overall the rows an array
for row in a:
    print(row)

# flatten the array aka make it act line print
for row in a.flat:
    print(row)

# stacking 2 arrays together
a = np.arange(6).reshape(3, 2)
b = np.arange(6, 12).reshape(3, 2)
print(a)

# veritcal stack the arrays
print(np.vstack((a, b)))

# horizontal stack the arrays
print(np.hstack((a, b)))

# split the array start by shaping it into 2 rows and 15 columns horizonal split it
a = np.arange(30).reshape(2, 15)
print(np.hsplit(a, 3))

# numpy vertical split
print(np.vsplit(a, 2))

# boolean result
a = np.arange(12).reshape(3, 4)
b = a > 4
print(b)

