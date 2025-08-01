contact = {}
while True:
    print("\n1.Add Contact\n2.View All\n3.Search\n4.Delete\n5.exit\n")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter name:")
        phone = int(input("Enter number:"))
        contact[name] = phone
        print("Contact saved")
    elif choice == "2":
        for name,phone in contact.items():
            print(f"{name}: {phone}")
    elif choice == "3":
        name_to_search = input("Enter name to search: ")
        if name_to_search in contact:
            print(f"{name_to_search} phone is: {contact[name_to_search]}")
        else:
            print("Name not found")
    elif choice == "4":
        name_to_delete = input("Enter name to delete: ")
        if name_to_delete in contact:
            del contact[name_to_delete]
            print("contact deleted")
        else:
            print("name not found")
    elif choice == "5":
        break
    else:
        print("Wrong input.. try again")