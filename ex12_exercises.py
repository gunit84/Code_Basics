#!python3

"""Dictionary and Tuple Exercise... """

__author__ = "Gavin Jones"

"""

# 1 Write a program that allows to store age of your family members.

# Program should ask to enter the person name and age
# Once you are done you should be able to input the name of the person and retrieve the age.
# Now print Name of all your Family Members along with their ages.

# Blank Dict to start
family = {}

#  Run the Program get Family Member Input 4 Times
for member in range(4):
    name = input("Please enter your name: ").capitalize()
    age = int(input("Please enter your age: "))
    family[name] = age

# Find out who's age they want:
personName = input("Please enter the Members Age your after: ").capitalize()


#  Run the Function to get the Family Members Age
def get_member_age(personName):
    if personName == "Gavin":
        return "Gavin's Age is", family["Gavin"]
    elif personName == "Hayley":
        return "Hayley's Age is", family["Hayley"]
    elif personName == "Marcia":
        return "Marcia's Age is", family["Marcia"]
    elif personName == "David":
        return "David's Age is", family["David"]
    else:
        return "This person is NOT a member of the Family!"


# Run the Program:
familyFunction = get_member_age(personName)
print(familyFunction)

# Prints the Family Member and there Ages!
for k, v in family.items():
        print("Name:", k, "Age:", v)

"""

"""
# 2  Write a function called add_and_multiply takes two numbers as input and return the sum and multiplication
# as 2 seperate numbers


def add_and_multiply(num1, num2):
    sum_task = num1 + num2
    multiplication_task = num1 * num2
    tupleResult = (sum_task, multiplication_task)
    return tupleResult


# Run the Program Get the Users Input
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a number: "))

# Save the function as a Variable
result = add_and_multiply(num1, num2)

# Run the function
print(result)
"""
