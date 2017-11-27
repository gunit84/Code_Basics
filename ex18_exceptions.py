#!python3

"""Python Exceptions... """

__author__ = "Gavin Jones"

try:
    x = input("Enter Number 1: ")
    y = input("Enter Number 1: ")
    z = int(x) / int(y)
    print("Division is {}".format(z))

# His Exception example
except Exception as e:
    print('exception occured: ', e)
# Cannot divide by Zero
except ZeroDivisionError:
    print("Sorry you cannot divide by Zero6")
