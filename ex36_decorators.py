#!python3

"""Learning about Python Decorators... """

__author__ = "Gavin Jones"

import time


# Wrapper a Function that will have a function inside it to give us the timing of the function.
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + "mil sec")
        return result
    return wrapper


# added decorator to time the function
@time_it
# function to square numbers
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result


# added decorator to time the function
@time_it
# function to square numbers
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result


array = range(1, 100000)

# Run the functions
out_square = calc_square(array)
out_cube = calc_cube(array)
