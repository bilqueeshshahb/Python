#3-6.write a python program that creates aclass & inherit into another class(base class:student with rollno,name,gender,age)(derived class:course with coursename,duration,fee)

# Base class: Student
class Student:
    def __init__(self, rollno, name, gender, age):
        self.rollno = rollno
        self.name = name
        self.gender = gender
        self.age = age
    
    def display_student(self):
        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Age:",self.age)

# Derived class: Course (inherits from Student)
class Course(Student):
    def __init__(self, rollno, name, gender, age, coursename, duration, fee):
        # Call the parent class constructor
        super().__init__(rollno, name, gender, age)
        self.coursename = coursename
        self.duration = duration
        self.fee = fee
    
    def display_course(self):
        print("Course Name:" ,self.coursename)
        print("Duration:", self.duration)
        print("Fee:" ,self.fee)
    
    def display_all(self):
        print("--- Student Details ---")
        self.display_student()
        print("\n--- Course Details ---")
        self.display_course()

# Main program
print("=" * 40)
print("INHERITANCE DEMONSTRATION")
print("=" * 40)

# Create an object of derived class Course
student_course = Course(
    rollno=101,
    name="John Doe",
    gender="Male",
    age=20,
    coursename="Python Programming",
    duration="3 months",
    fee=5000
)

# Display all information
student_course.display_all()

print("\n" + "=" * 40)
print("Another Example:")
print("=" * 40)

# Create another object
student_course2 = Course(
    rollno=102,
    name="Jane Smith",
    gender="Female",
    age=22,
    coursename="Data Science",
    duration="6 months",
    fee=8000
)

student_course2.display_all()
