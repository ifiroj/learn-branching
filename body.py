from main import *

while True:
    print("Select an option")
    print("1. Add")
    print("2. Show")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")
    choice = int(input())

    if choice==1:
        adding()
    elif choice==2:
        displaying()
    elif choice==3:
        searching()
    elif choice==4:
        updating()
    elif choice==5:
        deleting()
    elif choice==6:
        break
    else:
        print("Invalid Option")