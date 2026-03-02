#3-2.write a program to to create a class for student with rollno,name, age,genclass Student:
      # student1.DisplayStudent()der and methods name AddStudent() and DisplayStudent()
class Student:
    """Student class with rollno, name, age, gender"""
    
    def __init__(self):
        self.rollno = ""
        self.name = ""
        self.age = 0
        self.gender = ""
    
    def AddStudent(self, rollno, name, age, gender):
        """Add student details"""
        self.rollno = rollno
        self.name = name
        self.age = age
        self.gender = gender
        print("✓ Student added successfully!")
    
    def DisplayStudent(self):
        """Display student details"""
        print("\n" + "="*30)
        print("       STUDENT DETAILS")
        print("="*30)
        print(f"Roll No   : {self.rollno}")
        print(f"Name      : {self.name}")
        print(f"Age       : {self.age}")
        print(f"Gender    : {self.gender}")
        print("="*30)

# Main program
if __name__ == "__main__":
    # Create student object
    student1 = Student()
    
    # Add student details
    student1.AddStudent("101", "John Smith", 20, "Male")
    
    # Display student details
    student1.DisplayStudent()
