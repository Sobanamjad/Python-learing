class Person:
    __name = "Annonymus"

    def __hello(self):
        print("Hello User!")

    def welcome(self):
        self.__hello()


p1 = Person()
print(p1.welcome())

# Ingeritance
class Car:
    @staticmethod
    def start():
        print("Car Started!")
    @staticmethod
    def stop():
        print("Car Stopped!")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")
print(car1.start())
print(car2.stop())
