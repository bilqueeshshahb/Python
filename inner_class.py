#3-4.write a program to make uyse of inner class.
class Student:
    """Outer class - Student"""
    
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.address = None  # Will hold inner class object
    
    def AddStudent(self):
        """Add student details"""
        print("Student: ",self.name, "Roll No:", self.rollno)
    
    # Inner class - Address
    class Address:
        """Inner class - Address details"""
        
        def __init__(self, street, city, state, pincode):
            self.street = street
            self.city = city
            self.state = state
            self.pincode = pincode
        
        def DisplayAddress(self):
            """Display address details"""
            print("Address:",self.street, self.city, self.state , self.pincode)

# ============================================
# MAIN PROGRAM
# ============================================

print("=" * 40)
print("    INNER CLASS DEMONSTRATION")
print("=" * 40)

# Create outer class object
student1 = Student("John Smith", "101")

# Create inner class object using outer class object
addr1 = student1.Address("123 Main Street", "New York", "NY", "10001")

# Link inner class to outer class
student1.address = addr1

# Display details
print("\n--- Student Details ---")
student1.AddStudent()
print("\n--- Address Details ---")
addr1.DisplayAddress()
