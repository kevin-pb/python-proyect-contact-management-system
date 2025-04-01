import ast

def read_db(direction="db\contacts.txt"):
    with open(direction, "r") as contacts:
        return contacts.read().strip()

def read_db_like_dictionary(direction="db\contacts.txt"):
    with open(direction, "r") as contacts:
        contacts_read = "{" + contacts.read().strip() + "}"
    return ast.literal_eval(contacts_read) if contacts_read != "{}" else {}

def write_db(thing_to_write, direction="db\contacts.txt"):
    with open(direction, "a") as contacts:
        if read_db():    
            contacts.write(",\n" + str(thing_to_write))
        else:    
            contacts.write(str(thing_to_write))

def get_db_lines(direction="db\contacts.txt"):
    with open(direction, "r") as contacts:  
        return contacts.readlines()

def dictionary_define(name, phone_number, email):
    return {"name": name, "phone_number": phone_number, "email": email}

def delete(thing_to_delete, direction="db\contacts.txt"):
    database_read_like_dictionary = read_db_like_dictionary()
    if thing_to_delete in database_read_like_dictionary:
        del database_read_like_dictionary[thing_to_delete]
    
    with open(direction, "w") as contacts:
        contacts.write(",\n".join(f"'{k}':{v}" for k, v in database_read_like_dictionary.items()))

def overwrite(identifier, overwrite, direction="db\contacts.txt"):
    database_read_like_dictionary = read_db_like_dictionary()
    database_read_like_dictionary[identifier] = overwrite
    
    with open(direction, "w") as contacts:
        formatted_entries = [f"'{k}':{v}" for k, v in database_read_like_dictionary.items()]
        contacts.write(",\n".join(formatted_entries))
