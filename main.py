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
        print("Adding")
    elif choice==2:
        print("Showing")
    elif choice==3:
        print("Searching")
    elif choice==4:
        print("Updating")
    elif choice==5:
        print("Deleting")
    elif choice==6:
        break
    else:
        print("Invalid Option")