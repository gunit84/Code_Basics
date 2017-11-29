#!python3

"""Exercise 10 Questions... """

__author__ = "Gavin Jones"

"""

# 1 After flipping a cont 10 times you got the result in the list result, use a for loop figure out the count
# for heads.

# result list
result = ["heads", "tails", "tails", "heads", "tails", "heads", "heads", "tails", "tails", "tails"]

# total heads in a new list.
numberOfHeads = []

for answer in result:
    if answer == "heads":
        numberOfHeads.append(answer)
    else:
        pass
    
print("The number of heads in the result list is {}".format(len(numberOfHeads)))

"""

"""

# 2 Write a Program that asks you to eneter the expense amount and tell you the Month in which that expense occured.

expense_list = [2340, 2500, 2100, 3100, 2980]

userAmount = int(input("Please enter the expense amount: "))

if userAmount == expense_list[0]:
    print("The expense occured in January")
elif userAmount == expense_list[1]:
    print("The expense occured in February")
elif userAmount == expense_list[2]:
    print("The expense occured in March")
elif userAmount == expense_list[3]:
    print("The expense occured in April ")
elif userAmount == expense_list[4]:
    print("The expense occured in May")
else:
    print("That amount is not in our expense list!")

"""

"""

# 3 Write a Program that prints the following shape!

*
**
***
****
*****


for star in range(6):
    print("*" * star)

"""





