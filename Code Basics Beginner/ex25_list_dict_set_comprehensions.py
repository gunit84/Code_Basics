#!python3

"""Python3 List,Set,Dict Comprehensions... """

__author__ = "Gavin Jones"

#  Step 1 Dictionary Comprehension
numbers = [1, 2, 3, 4, 5, 6, 7]

# Find the Even Numbers
evenNumbers = [x for x in numbers if x % 2 == 0]
print(evenNumbers)

# Square all these numbers
squareNumbers = [x ** 2 for x in numbers]
print(squareNumbers)

# Set Comprehension
testSet = set([1, 2, 3, 4, 5, 6, 7, 7, 2])
evenSet = {i for i in testSet if i % 2 == 0}
print(evenSet)

# Dictionary Comprehension and zip
# Below is Zip where each of the elements in the list join up with tuple output
cities = ["mumbai", "new york", "paris"]
countries = ["india", "usa", "france"]

for info in zip(cities, countries):
    print(info)

# Dictionary Comprehension by joining the 2 Lists and Producing a Key Value Pair
testDict = {city: country for city, country in zip(cities, countries)}
print(testDict)
