contacts = {}

def show_menu():
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact added successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            for name, details in contacts.items():
                print(f"\nName: {name}")
                for key, value in details.items():
                    print(f"{key}: {value}")

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(contacts[name])
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice.")