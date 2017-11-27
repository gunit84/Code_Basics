#!python3

"""Python Explanation of the if __name__ == "__main__" line... """

__author__ = "Gavin Jones"


def calculate_area(base, height):
    print("__name__:", __name__)
    return 1 / 2 * (base * height)


if __name__ == '__main__':
    print("I am in Ex17_if_main.py")
    a = calculate_area(10, 20)
    print("area:", a)
