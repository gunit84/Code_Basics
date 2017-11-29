#!python3

"""Multiprocessing sharing data between processes... aka global variables"""

__author__ = "Gavin Jones"

import multiprocessing


# Calculate the square of Numbers
def calc_square(numbers, result, v):
    v.value = 5.67
    for idx, n in enumerate(numbers):
        result[idx] = n * n


if __name__ == '__main__':
    numbers = [2, 3, 5]
    # Shared Memory Variable (It uses i for integer and 3 for the amount of elements)
    result = multiprocessing.Array("i", 3)
    v = multiprocessing.Value("d", 0.0)
    p = multiprocessing.Process(target=calc_square, args=(numbers, result, v))

    p.start()
    p.join()

    print(v.value)
