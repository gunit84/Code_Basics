#!python3

"""Classes Exercises... """

__author__ = "Gavin Jones"


class Human:
    # Calls this METHOD on every instance of a class.
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.occupation == "tennis player":
            print("Play Tennis")
        elif self.occupation == "actor":
            print("shoots film")

    def speaks(self):
        print(self.name, "says how are you?")


# Instances of the class
tom = Human("Tom Cruise", "actor")
maria = Human("Maria Sharap", "tennis player")

# Calls the Objects
tom.speaks()
tom.do_work()

maria.speaks()
maria.do_work()
