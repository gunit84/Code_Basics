#!python3
# Ch 9 Exercises

indian = ["samosa", "daal", "naan"]
chinese = ["egg role", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]

userDish = input("Please enter a dish: ")

if userDish in indian:
    print("User's dish is Indian")
elif userDish in chinese:
    print("User's dish is Chinese")
elif userDish in italian:
    print("User's dish is in Italian")
else:
    print("I am not sure where the User's dish is from..?")

