import ast

def read_db(direction="db\contacts.txt"):
    contacts = open(direction, "r")
    contacts_read = contacts.read()
    contacts.close
    return contacts_read

def read_db_like_dictionary(direction="db\contacts.txt"):
    contacts = open(direction, "r")
    contacts_read = contacts.read()
    contacts_read = "{" + contacts_read + "}"
    contacts_read = ast.literal_eval(contacts_read)
    contacts.close
    return contacts_read

def write_db(thing_to_write, direction="db\contacts.txt"):
    contacts = open(direction, "a")
    if read_db() != "":    
        contacts.write("," + "\n" + str(thing_to_write))
    if read_db() == "":    
        contacts.write(str(thing_to_write))
    contacts.close
    
def over_write_db(thing_to_write, direction="db\contacts.txt"):
    contacts = open(direction, "w")   
    
    contacts.close

def dictionary_define(name, phone_number, email):
    dictionary = {"name": name, "phone_number": phone_number, "email": email}
    return dictionary

