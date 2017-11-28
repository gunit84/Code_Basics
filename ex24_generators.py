#!python3

"""Python3 Information about Generators... """

__author__ = "Gavin Jones"


def remote_control_next():
    yield "cnn"
    yield "espn"


itr = remote_control_next()
print(next(itr))
print(next(itr))

# Runs a for loop on the actual generator function.
for item in remote_control_next():
    print(item)
