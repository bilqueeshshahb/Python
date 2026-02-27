#9.write a program to do student operations using menu as follows:
#1add
#2search
#3.list all
#4.update
#5.delete
#6exit.

students =[]

while True:
    print("1. add student")
    print("2. search student")
    print("3.list all student")
    print("4.update student")
    print("5.delete student")
    print("6.exit")

    choice = input ("enter your choice(1-6):")

    if choice =='1':
        roll = input("enter roll no:")
        name = input("enter name:")
        grade = input ("enter grade:")
        students.append({"roll":roll,"name":name,"grade":grade})
        print("students added successfully.")

    elif choice =='2':
        search_roll = input("enter roll no to search:")
        found = False
        for s in students:
            if s['roll'] == search_roll:
                print(f"found!name: {s['name']},grade:{s['grade']}")
                found = True
                break
        if not found:
            print("students not found.")

    elif choice == '3':
        if not students:
            print("no records found:")
        for s in students:
            print(f"roll:{s['roll']} | name:{s['name']} |grade:{s['grade']}")

    elif choice == '4':
        up_roll = input("enter roll no to update")
        for s in students:
            if s['roll'] ==up_roll:
                s['name'] = input("enter new name")
                s['grade'] = input("enter new grade")
                print("record updated")
                break
            else:
                print("roll no not found.")

    elif choice == '5':
         del_roll =input("enter roll no to delete")
         for s in students:
             if s['roll']== del_roll:
                 students.remove(s)
                 print("students deleted")
                 break
             else:
                 print("roll no not found.")
    elif choice == '6':
         print("exit program.")
         break
    else:
         print("invalid choice")
         
                
                

            
    
