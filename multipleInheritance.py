#3-7.use appropriate functions for each classwrite a program to display MRO using multiple inheritance.
#multiple inheritance can be done as per your choice.

# Base Class 1
class Father:
    def show(self):
        print("Father's show() method")

# Base Class 2
class Mother:
    def show(self):
        print("Mother's show() method")

# Child Class inheriting from Father and Mother
class Child(Father, Mother):
    def show(self):
        print("Child's show() method")
        super().show()   # Calls next method in MRO

# Creating object
obj = Child()

# Calling method
obj.show()

# Displaying MRO
print("\nMethod Resolution Order (MRO):")
for cls in Child.__mro__:
    print(cls)
       
