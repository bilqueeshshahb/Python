#11.write a program to create function which shall accept any no. of arguements & display total of all the nos. given as arguements.

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(40,10))
print(sum_all(10,20,30,40))
