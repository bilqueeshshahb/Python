#5.write a program to enter 10 numbers & display largest odd numbers.
numbers=[12,45,7,22,98,33,56,4,11,89]

evens=[n for n in numbers if n%2==0]
odds=[n for n in numbers if n%2!=0]

print("numbers:", numbers)
print("largest even:", max(evens)if evens else "none")
print("largest odd:",max(odds)if odds else "none")

