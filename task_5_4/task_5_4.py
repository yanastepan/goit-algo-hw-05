from typing import Callable, Any

# the fuction takes the user input string and splits it into words using the split() method.
# it returns the first word as a cmd command and the rest as a list of *args arguments.
def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()           # removes unnecessary spaces around the command and converts it to lowercase.
    return cmd, args


# a decorator function to handle common input errors for contact management functions
# as an argument takes the function, which is supposed to be decorated
def input_error(func: Callable) -> Callable:
    # innner function that wraps the original function with error handling
    # as arguments takes list of arguments passed to the original function and dictionary of contacts
    # returns the result of the original function or an error message
    def inner(args: list, contacts: dict) -> Any:
        
        try:                                # attempt to execute the original function with provided arguments
            return func(args, contacts)
        except ValueError:                  # handle ValueError and return a specific error message
            return "Give me name and phone please."
        except KeyError:                    # handle KeyError and return a specific error message
            return "This contact doesn't exist in your contact list."
        except IndexError:                  # handle IndexError and return a specific error message
            return "Are you sure about this action?"

    return inner                            # return the inner function with error handling




# the function takes str arguments (name an phone) and the dictionary of the contact list
# it adds the name and the phone to the dictionary, creating a contact list for a user
@input_error
def add_contact(args: list, contacts: dict) -> dict:

    name, phone = args              # the argumnents are splitted into 2 variables
    if phone.isdigit():             # check if the phone number contains digits only
        name = name.strip().lower() # removes unnecessary spaces around the command and converts it to lowercase
        contacts[name] = phone      # if so, add the contact with the key as the name and value as a phone
        return "Contact added."     # confirming the action by outputting the message for the user 


# the function takes str arguments (name an phone) and the dictionary of the contact list
# it changes the phone number under the existing name and add it back to the dictionary, modifying a contact list for a user
@input_error
def change_contact(args: list, contacts: dict) -> dict:
    name, phone = args                  # the argumnents are splitted into 2 variables
    name = name.strip().lower()         # removes unnecessary spaces around the command and converts it to lowercase
    if name in contacts:                # checking if the name is existing in the user contact list (dictionary with the names and phones)
        if phone.isdigit():             # check if the phone number contains digits only
            contacts[name] = phone      # if so, update the contact with the key as the name and value as a phone
            return "Contact updated."   # confirming the action by outputting the message for the user 
    else:
            return "You don't have this contact in your list to change. Please, create the contact first."



# the function takes the dictionary of the contact list
# it shows the entire contact list in the output for the user

def all_contacts(contacts: dict) -> str:
    contact_list = ""                               # the final return is going to be placed in this variable
    for key, value in contacts.items():             # issue the keys (names) and values (phone numbers) from the contact list (dict)
        contact_list += key + " - " + value + "\n"  # adding them to the str
    return contact_list


# the function takes str arguments (args == name) and the dictionary of the contact list
# it shows the phone number of the specific required name in the output for the user
@input_error
def show_phone(args: list, contacts: dict) -> str:
    name = args[0].strip().lower()      # convert name to lowercase
    return contacts[name]               # issue the value (phone) under the key (name) we need

