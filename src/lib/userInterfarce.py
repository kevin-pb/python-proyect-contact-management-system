import dbOperations as db

def ui():
    while True is True:
        if db.read_db() == "":
            db.write_db(input("Enter a identifier of the contact: ") + ":" + str(db.dictionary_define(input("Enter the name of the contact: "), input("Enter the phone number the contact: "), input("Enter the email of the contact: "))))
        else:
            print("Contacts options:")
            print("1-Show contacts")
            print("2-Add contact")
            print("3-Erase contact")
            print("4-Update contact")
            print("5-Exit")
            option = input("Chose an option: ")
            
            if int(option) == 5:
                break
            
            elif int(option) == 1:
                print(db.read_db())
            
            elif int(option) == 2:
                db.write_db("'" + input("Enter an identifier of the contact: ") + "'" + ":" + str(db.dictionary_define(input("Enter the name of the contact: "), input("Enter the phone number the contact: "), input("Enter the email of the contact: "))))
            
            elif int(option) == 3:
                try:
                    db.delete(input("Enter the identifier of the contact: "))                    
                except ValueError:
                    db.delete(int(input("Enter the identifier of the contact: ")))
            
            elif int(option) == 4:
                try:
                    db.overwrite(input("Enter the identifier of the contact: "), str(db.dictionary_define(input("Enter the new name of the contact: "), input("Enter the new phone number the contact: "), input("Enter the new email of the contact: "))))   
                except ValueError: 
                    db.overwrite(int(input("Enter the identifier of the contact: ", str(db.dictionary_define(input("Enter the new name of the contact: "), input("Enter the new phone number the contact: "), input("Enter the new email of the contact: "))))))
ui()