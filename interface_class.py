#3-9 write a program to create interface & utilize the same in another class.

from abc import ABC, abstractmethod

# Creating Interface
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


# Implementing Interface in another class
class Car(Vehicle):

    def start(self):
        print("Car starts with key")


# Creating object
obj = Car()
obj.start()
