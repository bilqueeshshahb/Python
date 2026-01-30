#unit-2 (1). write a program to display basic exception handling in python.

try:
    number = int(input("enter a number:"))
    result = 10 / number
    print(result)
except ZeroDivisionError:
    print("No.U cannot divdide by zero.")
except ValueError:
    print("That wasn't a valid number!")
    
