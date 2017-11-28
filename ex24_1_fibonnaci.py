#!python3

"""Python3 Fibonacci Sequence with Generators... """

__author__ = "Gavin Jones"


# Function for the Fibonacci Number
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# For Loop that runs on the Fibonnaci Function
for number in fib():
    if number > 50:
        break
    print(number)
