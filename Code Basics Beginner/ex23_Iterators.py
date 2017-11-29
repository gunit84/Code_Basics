#!python3

"""Python Exercise about Iterators... """

__author__ = "Gavin Jones"

# Custom List
customList = ["hey", "bro", "your", "awesome"]

# Going through the loop manually with iter function on the
iterate = iter(customList)
# Prints the next element in the list
print(next(iterate))
print(next(iterate))

# iterfunction in reverse on the list
iterateReverse = reversed(customList)
print(next(iterateReverse))
