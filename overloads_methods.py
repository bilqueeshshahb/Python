#3-10 write a program to overload addition & subtraction.(use appropriate methods to overload the same.
class Number:
    
    def __init__(self, value):
        self.value = value

    # Overloading + operator
    def __add__(self, other):
        return Number(self.value + other.value)

    # Overloading - operator
    def __sub__(self, other):
        return Number(self.value - other.value)

    def display(self):
        print("Value:", self.value)


# Creating objects
num1 = Number(20)
num2 = Number(10)

# Using overloaded operators
result_add = num1 + num2
result_sub = num1 - num2

# Display results
print("Addition Result:")
result_add.display()

print("Subtraction Result:")
result_sub.display()
