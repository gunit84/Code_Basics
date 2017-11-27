#!python3

""" For Loop Examples """

__author__ = "Gavin Jones"

exp = [2340, 2500, 2100, 3100, 2980]

# total variable
totalExpenses = 0

# example loop
for item in exp:
    totalExpenses += item
print("The total expenses are {}".format(totalExpenses))
