#!python3

"""Python 3 sets and frozen sets learning... """

__author__ = "Gavin Jones"

basket = {"orange", "apple", "mango", "apple", "orange"}
print(basket)

# Another example of creating a Set
newSet = set()

# Adding items to the set
newSet.add(1)
newSet.add(2)

# Print the set
print(newSet)

# FrozenSet example

numbers = [1, 2, 2, 3, 4, 3, 2, 4, 1, 8, 9]

fs = frozenset(numbers)
print(fs)

# fs.add(99)

# Set operators
x = {"a", "b", "c"}
y = {"a", "h", "g"}

print("a" in x)
print("g" in x)

for element in x:
    print(element)

# Union example to join both sets together, does not print duplicates
print(x | y)

# Intersection, aka what element is found in both sets
print(x & y)

# Difference, what elements are in x but not in y
print(x - y)

# Checks if there is a subset of another set
print(x < y)

x = {"h", "g"}
y = {"a", "h", "g"}

# Now it will appear as a subset due to matching elements
print(x < y)
