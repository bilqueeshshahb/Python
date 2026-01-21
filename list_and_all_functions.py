#7.write a program to create alist & perform various operations on list.
my_list=[]

while True:
    print("\n---list operations menu---")
    print("1.add an element")
    print("2.remove an element")
    print("3.display the list")
    print("4.check list length")
    print("5.clear the list")
    print("6.exit")

    choice =(input("enter your choice(1-6):")
    if choice =='1':
        item=input("enter the item to add:")
        my_list.append(item)
        print(item,"has been added")
        
    elif choice =='2':
        item=(input("enter the item to remove:")
        if item in my_list:
            my_list.remove(item)
            print(item,"has been removed")
        else:
            print("item not found in the list.")
    elif choice =='3':
        print("current list:",my_list)
    elif choice =='4':
        print("total elements:",len(my_list))
    elif choice =='5':
        my_list.clear()
        print("list has been cleared.")
    elif choice =='6':
        print("exiting program. goodbye!")
        break
    else:
        print("invalid choice!please try again")
        
        
          
