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
    
def get_db_lines(direction="db\contacts.txt"):
    contacts = open(direction, "r")   
    contacts_lines = contacts.readlines()
    contacts.close
    return contacts_lines

def dictionary_define(name, phone_number, email):
    dictionary = {"name": name, "phone_number": phone_number, "email": email}
    return dictionary

def delete(thing_to_delete, direction="db\contacts.txt"):
    database_read_like_dictionary = read_db_like_dictionary()
    del database_read_like_dictionary[thing_to_delete]
    
    contacts = open(direction, "w")
    database_read = str(database_read_like_dictionary)
    database_read = database_read[1:len(database_read)-1]
    

    contacts.write(database_read)
    contacts.close

def overwrite(identifier, overwrite, direction="db\contacts.txt"):
    database_read_like_dictionary = read_db_like_dictionary()
    database_read_like_dictionary[identifier] = overwrite
    
    contacts = open(direction, "w")
    database_read = str(database_read_like_dictionary)
    database_read = database_read[1:len(database_read)-1]
    

    contacts.write(database_read)
    contacts.close