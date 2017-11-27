#!python3

"""Iterators Python... """

__author__ = "Gavin Jones"


class RemoteControl():
    def __init__(self):
        self.channels = ["HBO", "cnn", "abc", "espn"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        # When ever it reaches the end of the element it stops Iteration
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]


# Define the Instance / Object that the class Uses
remote = RemoteControl()
itr = iter(remote)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
