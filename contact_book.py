contacts = {}

def add_conatact():
    name = input("Enter your name:")
    phone = input("Enter your contact number:")
    email = input("Enter your email:")
    contacts[name] = {"phone":phone,"email":email}
    print(f"{name} added successfully!")

def view_contact():
    if not contacts:
        print("No contact found!")
    else:
        for name, info in contacts.items():
            print(f"\nName: {name}")
            print(f"\nPhone: {info['phone']}")
            print(f"\nEmail: {info['email']}")

def search_contact():
    name = input("Enter name to search:")
    if name in contacts:
        print(f"\nName: {name}")
        print(f"\nPhone: {contacts[name]['phone']}")
        print(f"\nEmail: {contacts[name]['email']}")
    else:
        print("Contact not found!")
def delete_contact():
    name = input("Enter name to delete:")
    if name in contacts:
        del contacts[name]
        print(f"{name} delete successfully!")
    else:
        print("Contact not found!")
def update_contact():
    name = input("Enter name to update:")
    if name in contacts:
        phone = input("Enter new phone:")
        email = input("Enter new email")
        contacts[name] = {"phone":phone,"email":email}
        print(f"{name} update successfully!")
    else:
        print("Contact not found!")

def main():
    while True:
        print("=====Contact-Book=====")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit ")

        choice = input("Enter your choice....")
        if choice == '1':
            add_conatact()
        elif choice == '2':
            view_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice try again!")
main()