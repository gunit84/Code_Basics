#!python3

""" Range Function """

__author__ = "Gavin Jones"


for number in range(1, 11):
    print(number * number)
print()

# Next Code

exp = [2340, 2500, 2100, 3100, 2980]
total = 0


"""The reason we have to add +1 is because range starts at 0 and len starts at 1 """
for number in range(len(exp)):
    print("Month:", (number + 1), "Expense: ", exp[number])
    total += exp[number]
print()
print("The total of expenses is {}".format(total))
