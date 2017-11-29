#!python3

"""For Loop using the break statement """

__author__ = "Gavin Jones"

keyLocation = "chair"

locations = ["garage", "living room", "chair", "closet"]

# Search for the Keys!
for item in locations:
    if item == keyLocation:
        print("The Keys have been found at {} !!!".format(keyLocation))
        break
    else:
        print("Cannot find the Keys at", item)
