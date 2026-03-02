#3-8 write a program to create a abstract class with one method.
from abc import ABC, abstractmethod

# Creating Abstract Class
class Animal(ABC):

    @abstractmethod
    def sound(self):   # Abstract Method
        pass


# Creating Child Class
class Dog(Animal):

    def sound(self):
        print("Dog barks")


# Creating Object
obj = Dog()
obj.sound()
