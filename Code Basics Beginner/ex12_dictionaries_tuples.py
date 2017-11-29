#!python3

"""Learning Dictionaries and Tuples... """

__author__ = "Gavin Jones"

# test dictionary

d = {"tom": 12345, "kelly": 23456, "gavster": 99868}

# access element
print(d["gavster"])

# add element to the dictionary
d["robbo"] = 121212
print(d)

# delete an entry from a dictionary
del d["robbo"]
print(d)

# print all the directory values
for values in d.values():
    print(values, end=" ")
print()

# print all keys and values
for items in d.items():
    print(items)

# His example to get keys and values
for key in d:
    print("key:", key, "value:", d[key])
print()

# another example
for k, v in d.items():
    print("key:", k, "value:", v)
print()

# check if element in dictionary
print("gavster" in d)

# clear the dictionary
d.clear()
print(d)

# tuples
point = (5, 9)

# prints 5
print(point[0])
print(point[1])







