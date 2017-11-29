#!python3

"""Multiprocessing Pool... """

__author__ = "Gavin Jones"

from multiprocessing import Pool


# test function that calculates the square of numbers
def f(n):
    return n * n


# Program entry point
# This divides the function between all the Cores 0, 1, 2, 3
if __name__ == '__main__':
    # Object of Pool Class
    p = Pool(processes=3)
    #
    result = p.map(f, [1, 2, 3, 4, 5])
    for n in result:
        print(n)
