#!python3

"""Python3 Multithreading... """

__author__ = "Gavin Jones"

import time


# Calculate the square of Numbers
def calc_square(numbers):
    print("calculate square numbers")
    for number in numbers:
        time.sleep(0.2)
        print("squares: ", number * number)
    print()


# Calculate the Cube of the Numbers
def calc_cube(numbers):
    print("calculate cube of numbers")
    for number in numbers:
        time.sleep(0.2)
        print("cube:", number * number * number)
    print()


# List used for input
arr = [2, 3, 8, 9]

# time variable to calculate speed
t = time.time()

# run the functions
calc_square(arr)
calc_cube(arr)

# calculates the time taken
print("done in ...", time.time() - t)
