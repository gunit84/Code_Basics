#!python3

"""Basic Function for addition... """

__author__ = "Gavin Jones"


def sum(a, b):
    """A function about sum"""
    return a + b


# The Sum Result
sumResult = sum(3, 4)
print("The result of the sum is {}".format(sumResult))

# Call the docstring
funcHelp = help(sum)

print(funcHelp)