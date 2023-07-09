# Lab_3.2 sub.ex

import os

def clear_screen():
    input("\nPress Enter to continue: ")
    if os.name == "nt": 
        os.system("cls")
    else:
        os.system("clear")

def menu():
    print("\nChoose an operation:\n[v] View contacts\n[a] Add contact\n[d] Delete contact\n[q] Quit")
    return input("\nSelect an option (v/a/d/q): ").lower()

def view_contacts(contacts):
    print("\nContacts:")
    for i, (name, number) in enumerate(contacts):
        print(f"{i+1}. {name} - {number}")

def add_contact(contacts):
    name = input("\nEnter name: ")
    number = input("Enter contact number: ")
    contacts.append((name, number))
    print(f"\n{name} - {number} has been added to contacts.")
    return contacts

def delete_contact(contacts):
    view_contacts(contacts)
    try:
        idx = int(input("\nEnter the ID of the contact to delete: ")) - 1
        if idx < 0 or idx >= len(contacts):
            print("\nPlease enter a valid ID!")
            return contacts
        name, number = contacts.pop(idx)
        print(f"\n{name} - {number} has been removed from contacts.")
        return contacts
    except ValueError:
        print("\nPlease enter a valid ID!")
        return contacts

def main():
    contacts = [("Bibek","123"), ("Shah","456")]

    while True:
        option = menu()

        if option == 'v':
            view_contacts(contacts)
        elif option == 'a':
            contacts = add_contact(contacts)
        elif option == 'd':
            contacts = delete_contact(contacts)
        elif option == 'q':
            print("\nGoodbye.")
            break
        else:
            print("\nInvalid option. Try again.")
        
        clear_screen()

if __name__ == "__main__":
    main()
