#3-3write a program to make use of class method and instance method.
class MathOperations:
    # Class variable
    counter = 0
    
    def __init__(self):
        MathOperations.counter += 1
    
    # Instance method
    def square(self, num):
        return num * num
    
    # Class method
    @classmethod
    def get_counter(cls):
        return cls.counter

# Usage
m1 = MathOperations()
m2 = MathOperations()

print("Instance method - 5 squared:", m1.square(5))
print("Instance method - 10 squared:", m2.square(10))
print("Class method - Object count:", MathOperations.get_counter())
