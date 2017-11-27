#!python3

"""Python Exercise with JSON... """

__author__ = "Gavin Jones"

import json

# Dictionary Example as JSON
# Prefers dict() over {} for a blank dictionary
book = dict()

book["tom"] = {
    "name": "tom",
    "address": "1 red street, NY",
    "phone": 9898989898
}

book["bob"] = {
    "name": "bob",
    "address": "1 green street, NY",
    "phone": 9898989897
}

jsonDump = json.dumps(book)
print(jsonDump)

# Write the Dump to a File:
with open("book.txt", "w") as file:
    file.write(jsonDump)

# Read the File
with open("book.txt", "r") as file_read:
    jsonRead = file_read.read()
print(jsonRead)
