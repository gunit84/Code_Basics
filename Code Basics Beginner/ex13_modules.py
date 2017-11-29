#!python3

"""Learning Modules... """

__author__ = "Gavin Jones"

import sys

import functions as f

# Add the current directory to your Python Systems PATH so it can locate the file aka Module
sys.path.append("D:\PycharmProjects\Projects\Projects_Learning\Code Basics")

squareArea = f.calculate_square_area(5)
triangleArea = f.calculate_triangle_area(5, 10)

# Print the results
print("The Triangle Area is: {}".format(triangleArea))
print("The Square Area is: {}".format(squareArea))
