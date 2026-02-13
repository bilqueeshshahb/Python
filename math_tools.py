#4.create a module with 4 functions of ur choice.import & use the functions using module in different ways.

import math_tools

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def greet(name):
    return "Hello",name, "welcome to my module."

print(math_tools.add(10,5))
print(math_tools.sub(10,5))
print(math_tools.mul(10,5))
print(math_tools.greet("priya"))
