#3.write a program to enter marks of 4 subjects& display result(result shall include total,marks and percentage.)
mark1=float(input("enter mark 1(out of 100): "))
mark2=float(input("enter mark 2(out of 100): "))
mark3=float(input("enter mark 3(out of 100): "))
mark4=float(input("enter mark 4(out of 100): "))

total_marks_obtained=mark1 +mark2 +mark3+mark4
total_possible_marks =400
percentage=(total_marks_obtained/total_possible_marks) * 100

if percentage>= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 50:
    grade = 'D'
else:
    grade = 'Fail'

print("-" * 30)
print(f"total marks obtained: {total_marks_obtained} out of {total_possible_marks}")
print(f"percentage: {percentage:.2f}%")
print(f"grade: {grade}")
print("-" *30)
    
