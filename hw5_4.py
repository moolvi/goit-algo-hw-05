def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as err:
            return f'{err}'
        except IndexError as err:
            return f'{err}'
        except KeyError as err:
            return f'{err}'
        except Exception as err:
            return f'{err}'

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        raise ValueError ("The contact already exists. Addendum canceled.")
    else:
        contacts[name] = phone
        return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise ValueError(f'The phone by "{name}" isn\'t found.')

@input_error
def show_phone(name, contacts):
    if name in contacts:
        return (f'{name}: {contacts[name]}\n')
    else:
        raise ValueError (f'The phone by "{name}" isn\'t found.')

@input_error
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            for name, phone in contacts.items():
                print(f'{name}: {phone}')
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()