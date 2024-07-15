from task_5_4 import parse_input, add_contact, change_contact, all_contacts, show_phone

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            result = add_contact(args, contacts)
            if result:
                print(result)
        elif command == "change":
            result = change_contact(args, contacts)
            if result:
                print(result)
        elif command == "all":
            print(all_contacts(contacts))
        elif command == "phone":
            result = show_phone(args, contacts)
            if result:
                print(result)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
