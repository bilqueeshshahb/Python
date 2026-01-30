#10.write  aprogram to create a 4 lambda functions which shall accept 2 nos & 1 arithmetic operator.as per arithmertic operator related to lambda functions shall be invoked.

def calculator(num1,num2,operator):
    add = lambda x, y: x + y
    sub = lambda x, y: x - y
    mul = lambda x, y: x * y
    div = lambda x, y: x / y if y != 0 else"cannot dividd by zero"

    operations ={
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    if operator in operations:
        return operations[operator](num1, num2)
    else:
        return "invalid operator"

    print(calculator(10,5,"+"))
    print(calculator(10,5,"-"))
    print(calculator(10,5,"*"))
    print(valculator(10,5,"/"))
    
