#!python3

"""Print square of numbers 1 to 5 EXCEPT even Numbers... """

__author__ = "Gavin Jones"

for number in range(1, 6):
    if number % 2 == 0:
        continue
    else:
        print("Odd Number Squared {}:".format(number), number ** 2)
