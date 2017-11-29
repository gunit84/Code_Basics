#!python3

"""Python3 Multithreading... """

__author__ = "Gavin Jones"

import threading
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


# List used for input
arr = [2, 3, 8, 9]

# time variable to calculate speed
t = time.time()

# Use multithreading on the functions
t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

# Start the threads, which will execute the threads in parallel
t1.start()
t2.start()

# Join, waits until the Thread is finished
t1.join()
t2.join()

# calculates the time taken
print("done in ...", time.time() - t)
