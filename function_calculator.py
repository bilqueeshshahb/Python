#9.write a program to create a function which accept 2 nos.& 1 arithmetic operator.

def calculator(num1,num2,operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
           return num1 / num2
        else:
            return "error: division by  zero"
    else:
        return "invalid operator"
