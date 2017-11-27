#!python3

"""Python Multiple Inheritance Example... """

__author__ = "Gavin Jones"


class Father():
    def skills(self):
        print('gardening, programming')


class Mother():
    def skills(self):
        print("cooking, art")


# Inherits from 2 SuperClasses above
class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("I love sports")


# The child object is Created from the class Child which inherits the methods from the Parent Classes
child = Child()
# Inherited from Father Class
child.skills()
