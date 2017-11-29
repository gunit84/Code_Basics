#!python3

"""Exercises from Ch 11... """

__author__ = "Gavin Jones"


"""
# 1) Area of a Triangle via a function

# User Input for the base and Height
base = int(input("Please enter the base of the Triangle: "))
height = int(input("Please enter the height of the Triangle: "))


def calculate_area():
    # A Function to calculate the Area of a Triangle
    area = 1/2 * (base * height)
    return "The Area of the Triangle is {}".format(area)


areaResult = calculate_area()

# Run the Function
print(areaResult)

"""

"""
# 2) Area of a Triangle via a function

def calculate_area():
    # User Input for the base and Height
    base = int(input("Please enter the base or width: "))
    height = int(input("Please enter the height or length: "))
    shape = input("Please enter the shape type: ").lower()
    if shape == "rectangle":
        areaRectangle = base * height
        return "The Area of the Rectangle is {}".format(areaRectangle)
    else:
        # A Function to calculate the Area of a Triangle
        areaTriangle = 1/2 * (base * height)
        return "The Area of the Triangle is {}".format(areaTriangle)


areaResult = calculate_area()
# Run the Function
print(areaResult)

"""

"""

# 3 Function to print the amount of stars entered by the user.


def print_pattern(number):
    for star in range(number + 1):
        print("*" * star)


# Run the function input ptior
number = int(input("Please enter the amount of stars you want printed: "))
print_pattern(number)

"""