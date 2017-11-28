#!python3

"""Python3 Multiprocessing Lock... """

__author__ = "Gavin Jones"

import multiprocessing
import time


def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        # puts lock on process
        lock.acquire()
        balance.value += 1
        # releases lock on process
        lock.release()


def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        # puts lock on process
        lock.acquire()
        balance.value -= 1
        # releases lock on process
        lock.release()


if __name__ == '__main__':
    # define the values for the process
    balance = multiprocessing.Value("i", 200)

    # Create a Lock
    lock = multiprocessing.Lock()

    # define the processes and there functions
    d = multiprocessing.Process(target=deposit, args=(balance, lock))
    w = multiprocessing.Process(target=withdraw, args=(balance, lock))

    # start the processes
    d.start()
    w.start()

    # wait till the processes have stopped.
    d.join()
    w.join()

    print(balance.value)
