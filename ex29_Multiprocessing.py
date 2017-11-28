#!python3

"""Insert Information Here about the Program you are creating... """

__author__ = "Gavin Jones"

import multiprocessing
import time


# Calculate the square of Numbers
def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        # cpu is idle when time.sleep is triggered
        time.sleep(0.2)
        print("squares: ", n * n)
    print()


# Calculate the Cube of the Numbers
def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        # cpu is idle when time.sleep is triggered
        time.sleep(0.2)
        print("cube:", n * n * n)
    print()


# Program Entry
if __name__ == '__main__':
    # time variable to calculate speed
    t = time.time()

    # The list we will pass into the function
    arr = [2, 3, 8, 9]

    # The Processes defined as Variables
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    #   Start the processes
    p1.start()
    p2.start()

    #   Join waits until execution of the processes is OVER...
    p1.join()
    p2.join()

    # calculates the time taken
    print("done in ...", time.time() - t)
