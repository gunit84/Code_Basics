#!python3

"""Python Class Inheritance... """

__author__ = "Gavin Jones"


class Vehicle:
    def general_usage(selfs):
        print("General use: transportation")


class Car(Vehicle):
    def __init__(self):
        print("I'm Car ")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("Specific Use: commute to work, vacation with family")


class Motorcycle(Vehicle):
    def __init__(self):
        print("I'm MotorCycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(selfs):
        print("For Cruising and having fun!")


# Calls the Car Class
carInfo = Car()
# Inherits the general usage function from Vehicle Class
carInfo.general_usage()
# Uses it's own specific method
carInfo.specific_usage()

# Calls the Motorcycle Class
motorcycleInfo = Motorcycle()
# Inherits from Vehicle class
motorcycleInfo.general_usage()
# Uses it's own class method
motorcycleInfo.specific_usage()

# Check the Instance and Issubclass of the Objects
# This Checks the Object is an Instance of a Class or subclass
# Checks to see if carinfo is the Object/Instance of the Car Class
print(isinstance(carInfo, Car))
# Checks to see if Class Car is the subclass (inherits) from the Vehicle class
print(issubclass(Car, Vehicle))
