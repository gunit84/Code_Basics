#!python3

"""File exercises... """

__author__ = "Gavin Jones"

f = open(r"D:\PycharmProjects\Projects\Projects_Learning\Code Basics\funny.txt", "r")
print(f.read())
f.close()

print()

# read all the lines as a new line.

f = open(r"D:\PycharmProjects\Projects\Projects_Learning\Code Basics\funny.txt", "r")
for line in f:
    print(line)
f.close()

# count all the lines turns it into a list

f = open(r"D:\PycharmProjects\Projects\Projects_Learning\Code Basics\funny.txt", "r")
for line in f:
    tokens = line.split(" ")
    print(len(tokens))
f.close()

# Best Method the "with" statement, closes the file automatically.
with open(r"D:\PycharmProjects\Projects\Projects_Learning\Code Basics\funny.txt") as f:
    print(f.read())
