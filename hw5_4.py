import re


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            return f'{error}'
        except IndexError as error:
            return f'{error}'
        except KeyError as error:
            return f'{error}'
        except Exception as error:
            return f'{error}'

    return inner


@input_error
def parse_input(user_input):
# Function return a list with arguments or a error code.

    if re.search(r'.*[" "].*[" "].*',  user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
    else:
        return [-1]
    commands = ('close', 'exit', 'hello', 'add', 'change', 'phone', 'all')
    if not cmd in commands:
        return [-2]
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    phone = re.sub(r'[^*#pw0-9]', r'', phone)
    phone = phone if phone[0] in '+*#pw' else f'+{phone}'

    if not re.search(r'[0-9][0-9][0-9]', phone):
        raise ValueError ('Too few digits in the number')
    contacts[name] = phone
    return 'Contact added.'


@input_error
def change_contact(args, contacts):
# Updates an existing contact or adds a new one.
    
    name, phone = args
    if name in contacts:
        result = add_contact(args, contacts)
        if contacts[name] == phone:
            return 'Contact updated.'
        else:
            return result
    else:
        return add_contact(args, contacts)


@input_error
def show_phone(name, contacts):
    if name in contacts:
        return (f'{name}: {contacts[name]}\n')
    else:
        raise ValueError (f'The phone by "{name}" isn\'t found.')


def main():
    contacts = {}
    
    print('Welcome to the assistant bot!')
    while True:
        if 'Hello' == input('Enter a command: '):
            print('How can I help you?')
            user_input = input('Enter a command: ')
            command, *args = parse_input(user_input)

            if command == -1 or command == -2:
                print('Invalid command')
            else:
                if command in ['close', 'exit']:
                    print('Good bye!')
                    break
                elif command == 'hello':
                    print('How can I help you?')
                elif command == 'add':
                    print(add_contact(args, contacts))
                elif command == 'change':
                    print(change_contact(args, contacts))
                elif command == 'phone':
                    print(show_phone(args, contacts))
                elif command == 'all':
                    for name, phone in contacts.items():
                        print(f'{name}: {phone}')
                else:
                    print('This feature will probably be available after updates.')

if __name__ == '__main__':
    main()