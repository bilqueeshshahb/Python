#8.Write a program to read a file which has marks entryof students & display details with total ,percentage & grade(consider a file which hascomma separated data with rollno,student name,mark1,mark2,mark3and mark4.)
import csv

def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def main():
    filename = 'students.csv'  # Assume the file is named 'students.csv'
    
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header if present (assuming first line is header)
            
            print(f"{'Roll No':<10} {'Name':<20} {'Total':<10} {'Percentage':<12} {'Grade':<5}")
            print("-" * 60)
            
            for row in reader:
                if len(row) != 6:
                    print(f"Invalid row: {row}")
                    continue
                
                rollno = row[0].strip()
                name = row[1].strip()
                try:
                    mark1 = float(row[2])
                    mark2 = float(row[3])
                    mark3 = float(row[4])
                    mark4 = float(row[5])
                except ValueError:
                    print(f"Invalid marks in row: {row}")
                    continue
                
                total = mark1 + mark2 + mark3 + mark4
                percentage = (total / 400) * 100
                grade = calculate_grade(percentage)
                
                print(f"{rollno:<10} {name:<20} {total:<10.2f} {percentage:<12.2f} {grade:<5}")
    
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
