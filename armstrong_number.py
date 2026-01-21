#4 write a program to enter 10number all armstrong numbers from those numbers.
num=int(input("enter a number: "))
n=num
power=len(str(num))
total=0

while n>0:
    digit=n%10
    total+=digit**power
    n//=10

if total==num:
    print("armstrong number")
else:
    print("not an armstrong number")
    
