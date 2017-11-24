#!python3

# Lists Learning

expenses = [2200, 2350, 2600, 2130, 2190]

febdiffJan = expenses[1] - expenses[0]

# a)
print("In February we spent ${} more dollars then January!".format(febdiffJan))

# b)
totalExpense = expenses[0] + expenses[1] + expenses[3]
print("The total expenses for the first quarter is ${}.".format(totalExpense))

# c)
amount = 2000 in expenses
print("The answer to whether we spent exactly $2000 in any month is {}.".format(amount))

# d
expenses.append(1980)
print(expenses)

# e
april = 2130
returnedItem = 200

newApril = april - returnedItem
expenses[3] = newApril

print(expenses)
