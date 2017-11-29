#!python3

"""Learning about Python Decorators... """

__author__ = "Gavin Jones"

import time


# function to square numbers
def calc_square(numbers):
    # start the timer
    start = time.time()
    result = []
    for number in numbers:
        result.append(number * number)
    # end the timer
    end = time.time()
    # gives the time it took in miliseconds.
    print("calc_square function took " + str((end - start) * 1000) + " mil sec")
    return result


# function to square numbers
def calc_cube(numbers):
    # start the timer
    start = time.time()
    result = []
    for number in numbers:
        result.append(number * number * number)
    # end the timer
    end = time.time()
    # gives the time it took in miliseconds.
    print("calc_square function took " + str((end - start) * 1000) + " mil sec")
    return result


array = range(1, 100000)

# Run the functions
out_square = calc_square(array)
out_cube = calc_cube(array)
