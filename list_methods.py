#8-(a)perform following operations on given string.
#1count number of vowels in given string.

text = "hello world"
vowels ="aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1
print("text=",text)        
print("number of vowels",count)

#8-(b)write a program to count length of string.do not use len()
text = "Hello World"
count = 0

for char in text:
    count+= 1

print("length is :", count)    


#8-(c)reverse string.
text = "python"
reversed_text = text[::-1]

print(reversed_text)

#8-(d)find & replace operations.
text = " i love grapes, grapes are my favourite!"
new_text = text.replace("grapes","mangoes")

print(new_text)

#8-(e)check whether string entered is palindrome or not.
word = "racecar"

if word == word[::-1]:
    print("It is a palindrome string.")
else:
    print("It is not a palindrome string.")
    




