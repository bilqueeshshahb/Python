#3.write aprogram to create an arithmetic exception and log the exception in system.

import logging
logging.basicConfig(filename='log.txt',level=logging.ERROR)

try:
    result = 10/0
except ZeroDivisionError:
    logging.error("Siple Math Error:U tried to divide by zero!")
    print("Error recorded in log.txt")
    
