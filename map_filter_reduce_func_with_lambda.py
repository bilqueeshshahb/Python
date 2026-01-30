#13.write a program to make use of map(),filter(),and reduce functions with context to lambda functions.

#1map()
nums=[1,2,3,4]
doubled = list(map(lambda x: x * 2,nums))
print(doubled)

#2filter()
nums=[1,2,3,4,5,6]
evens = list(filter(lambda x: x% 2 ==0,nums))
print(evens)

#3.reduce()
from functools import reduce
nums=[1,2,3,4]
product = reduce(lambda x, y: x * y,nums)
print(product)


