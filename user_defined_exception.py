class TooHighError(Exception):
    """ this error is raised when a number is over 100."""
    pass

def check_value(num):
    if num > 100:
        raise TooHighError("wait.The number is too big!keep it under 100.")
    else:
        print("success!",num, "it is a great choice.")

try:
    num = int(input("enter a small number:"))
    check_value(num)
except TooHighError as e:
    print("caught an error:",e)
except ValueError:
    print("that is not even a number.")
        
        
