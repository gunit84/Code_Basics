#!python3

"""Python Excpetions Advanced... Custom Exception """

__author__ = "Gavin Jones"


class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg

    def handle(self):
        print("Accident occured take a detour!: ", self.msg)


try:
    raise Accident("crash between two cars")
except Accident as e:
    e.handle()
