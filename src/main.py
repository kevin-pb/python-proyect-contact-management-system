import lib.dbOperations as db 

def ui():
    while True:
        if db.read_db() == "":
            identifier = input("Enter an identifier of the contact: ")
            name = input("Enter the name of the contact: ")
            phone_number = input("Enter the phone number of the contact: ")
            email = input("Enter the email of the contact: ")
            db.write_db(f"'{identifier}':{db.dictionary_define(name, phone_number, email)}")
        else:
            print("\nContacts options:")
            print("1 - Show contacts")
            print("2 - Add contact")
            print("3 - Erase contact")
            print("4 - Update contact")
            print("5 - Exit")
            
            option = input("Choose an option: ")

            if option == "5":
                break

            elif option == "1":
                print("\nCurrent Contacts:")
                print(db.read_db())

            elif option == "2":
                identifier = input("Enter an identifier of the contact: ")
                name = input("Enter the name of the contact: ")
                phone_number = input("Enter the phone number of the contact: ")
                email = input("Enter the email of the contact: ")
                db.write_db(f"'{identifier}':{db.dictionary_define(name, phone_number, email)}")

            elif option == "3":
                identifier = input("Enter the identifier of the contact: ")
                try:
                    db.delete(identifier)
                    print("Contact deleted successfully.")
                except KeyError:
                    print("Error: Contact not found.")

            elif option == "4":
                identifier = input("Enter the identifier of the contact: ")
                if identifier in db.read_db_like_dictionary():
                    name = input("Enter the new name of the contact: ")
                    phone_number = input("Enter the new phone number of the contact: ")
                    email = input("Enter the new email of the contact: ")
                    db.overwrite(identifier, db.dictionary_define(name, phone_number, email))
                    print("Contact updated successfully.")
                else:
                    print("Error: Contact not found.")

            else:
                print("Invalid option. Please choose a valid number.")

ui()