#6.Write a program to read a file which contains only numbers.display total of all the numbers with maximum and minimum numbers.

try:
    with open('numbers.txt', 'r') as file:
        content = file.read()

        numbers = [float(n) for n in content.split()]

        if numbers:
            total = sum(numbers)
            maximum = max(numbers)
            minimum = min(numbers)
            
            print("numbers found:", numbers)
            print("Total Sum:", total)
            print("Maximum number:", maximum)
            print("Minimum number:", minimum)
        else:
            print("The file is empty.")

except FileNotFoundError:
    print("Error: Please create 'numbers.txt' first.")
except ValueError:
    print("Error:The file contains something that is not a number.")
            
