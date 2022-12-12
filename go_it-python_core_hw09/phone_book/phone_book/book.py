phone_book = {'Artur': '0675195783',
              'Katia': '0974132811',
              'Valera': '0992581278',
              'Amanda': '0442563164',
              'Valeri': '0662015630'
              }


def main():
    """Main function"""

    while True:
        input_command = input('Enter command: ')

        if input_command in ('good bye', 'close', 'exit', 'bye', 'end'):
            print('Good bye!')
            break

        result = command_parser(input_command)
        print(result)


def input_error(func):
    """Exception handling decorator."""

    def inner(*args, **kwargs) -> str:
        """Internal decorator function."""

        try:
            result = func(*args, **kwargs)
            return result
        except (IndexError, KeyError, ValueError, TypeError):
            return '-' * 75 + '\nPlease check the command you entered!\n' \
                              'The "add" and "change" commands accept two parameters each (name and number).\n' \
                              'The "phone" command accepts (name).\n' + '-' * 75

    return inner


@input_error
def command_parser(input_command: str) -> str:
    """Processes a command entered by the user."""

    s_command = input_command.split(' ')
    s_command = [item.lower() for item in s_command if item not in ('', ' ')]
    input_command = ' '.join(s_command)
    command = ''
    data = ''
    for key in OPERATIONS:
        if input_command.startswith(key):
            command = key
            data = input_command[len(command):]
            break
    if data:
        return func_call(command)(data)
    return func_call(command)()


def func_call(command: str):
    """Call the function according to the entered command"""

    return OPERATIONS.get(command, unknown_command)


def unknown_command() -> str:
    """Response to an unknown command"""

    return '-' * 30 + '\nI do not understand you!\n' + '-' * 30


def hello_func() -> str:
    """Greeting function"""

    return '-' * 30 + '\nHi!\nHow can I help you?\n' + '-' * 30


@input_error
def add_func(data: str) -> str:
    """Adds a contact to the phone book."""

    name, phone = split_data(data)

    if name not in phone_book.keys():
        phone_book[name] = phone
        return '-' * 30 + f'\nNew contact has been added:\n[{name}]:[{phone}]\n' + '-' * 30
    else:
        return '-' * 30 + '\nSuch a contact already exists!\n' + '-' * 30


@input_error
def change_func(data: str) -> str:
    """Replaces a contact in the phone book."""

    name, phone = split_data(data)

    if name in phone_book.keys():
        old_number = phone_book[name]
        phone_book[name] = phone
        return '-' * 40 + f'\nThe contact number has been changed from:\n[{old_number}] to [{phone}]\n' + '-' * 40
    else:
        return '-' * 30 + '\nNo such contact exists!\n' + '-' * 30


@input_error
def search_func(name: str) -> str:
    """Displays the phone number for the specified name."""

    name = name.strip().title()
    if name in phone_book:
        number = phone_book[name]
        return '-' * 30 + f'\n[{name}]:[{number}]\n' + '-' * 30
    else:
        return '-' * 30 + '\nNo such contact found!\n' + '-' * 30


def show_all() -> str:
    """Displays the entire phonebook."""

    result = f'{"=" * 30}\n'

    for contact in phone_book.keys():
        result += '{:<12}: {:<15}|\n'.format(contact, phone_book[contact])

    return result + f'{"=" * 30}\n'


def split_data(data: str) -> (str, str):
    """Distribution of data by name and phone"""

    s_data = data.strip().split(' ')
    name = s_data[0].title()
    phone = s_data[1]
    if name.isnumeric():
        raise ValueError('Wrong name!')
    elif not phone.isnumeric():
        raise ValueError('Wrong phone!')
    return name, phone


OPERATIONS = {'hello': hello_func,
              'hi': hello_func,
              'add': add_func,
              'change': change_func,
              'phone': search_func,
              'show all': show_all
              }

if __name__ == '__main__':
    main()
