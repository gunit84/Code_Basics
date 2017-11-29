#!python3

"""Sharing Data Between Processes using queue... """

__author__ = "Gavin Jones"

import multiprocessing


def calc_square(numbers, q):
    for n in numbers:
        q.put(n * n)


if __name__ == '__main__':
    numbers = [2, 3, 4]

    # initialising the process and queue
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(numbers, q))

    # Start the Process and wait for it to end
    p.start()
    p.join()

    # Print the results from the queue
    while q.empty() is False:
        print(q.get())
