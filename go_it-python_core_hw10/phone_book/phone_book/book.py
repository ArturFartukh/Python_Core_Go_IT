from collections import UserDict


class AddressBook(UserDict):
    """Class AddressBook """
    def add_record(self, record):
        self.data[record.contact.value] = record

    def del_record(self, name):
        self.data.pop(name)

    def get_all_contacts(self):
        result = []
        for name in self.data.keys():
            phones = self.data[name]
            phones = phones.get_all_numbers()
            result.append({name: phones})
        return result


class Record:
    """Contact information"""
    def __init__(self, new_name, phone=None):
        if phone is None:
            phone = []
        self.contact = Name(new_name)
        self.phones = phone

    def __repr__(self):
        return 'Functions of class:\n\n' \
               'add_phone(new_phone: str)\n\n' \
               'change_phone(old: str, new: str)\n\n' \
               'del_phone(new_phone: str)\n\n' \
               'phone_in_contact(phone: str) -> bool\n\n' \
               'get_all_numbers(self) -> list\n\n'

    def add_phone(self, new_phone):
        self.phones.append(Phone(new_phone))

    def change_phone(self, old: str, new: str):
        for number in self.phones:
            if number.value == old:
                number.value = new

    def del_phone(self, del_phone):
        for number in self.phones:
            if number.value == del_phone:
                self.phones.remove(number)

    def phone_in_contact(self, phone) -> bool:
        for number in self.phones:
            if number.value == phone:
                return True
        return False

    def get_all_numbers(self) -> list:
        return [number.value for number in self.phones]


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    """Name field"""
    pass


class Phone(Field):
    """Phone field"""
    pass


def main():
    """Main function"""

    print('=' * 30 + '\nMain commands:\n'
                     'add - add new contact\\contact number\n'
                     'change - change contact number\n'
                     'del - delete contact\\number\n'
                     'phone - number search by name\n'
                     'show all - show all contacts\n'
                     'info - command information\n' + '=' * 30)
    while True:
        input_command = input('Enter command: ')

        if input_command.lower() in stop_list:
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
        except (IndexError, KeyError, ValueError, TypeError, AttributeError):
            return '-' * 75 + '\nPlease check the command you entered!\n' \
                              'The "add" and "change" commands accept two parameters each (name and number).\n' \
                              'The "phone" command accepts (name).\n' \
                              'Enter "info" for more information.\n' + '-' * 75

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

    if name not in book.data.keys() and phone:
        new_contact = Record(name)
        new_contact.add_phone(phone)
        book.add_record(new_contact)
        return '-' * 30 + f'\nNew contact has been added:\n[{name}]:[{phone}]\n' + '-' * 30
    elif name not in book.data.keys() and not phone:
        new_contact = Record(name)
        book.add_record(new_contact)
        return '-' * 30 + f'\nNew contact has been added:\n[{name}]\n' + '-' * 30

    contact = book.data[name]
    if not contact.phone_in_contact(phone) and phone:
        contact.add_phone(phone)
        return '-' * 30 + f'\nNumber [{phone}] has been added to contact: [{name}]\n' + '-' * 30
    elif contact.phone_in_contact(phone):
        return '-' * 30 + '\nSuch a phone number already exists!\n' + '-' * 30
    else:
        return '-' * 30 + '\nSuch a contact already exists!\n' + '-' * 30


@input_error
def change_func(data: str) -> str:
    """Replaces a contact in the phone book."""

    name, phone_old = split_data(data)

    if name in book.data.keys():
        contact = book.data[name]
        if contact.phone_in_contact(phone_old):
            phone_new = input('Please enter a new number: ')
            contact.change_phone(phone_old, phone_new)
            return '-' * 40 + f'\nThe contact number has been changed from:' \
                              f'\n[{phone_old}] to [{phone_new}]\n' + '-' * 40
        else:
            return '-' * 30 + '\nNo such phone number exists!\n' + '-' * 30
    else:
        return '-' * 30 + '\nNo such contact exists!\n' + '-' * 30


@input_error
def del_funk(data: str) -> str:
    name, phone = split_data(data)
    if name not in book.data.keys():
        return '-' * 30 + f'\nContact with name {name} not found!\n' + '-' * 30
    contact = book.data[name]
    if contact.phone_in_contact(phone):
        contact.del_phone(phone)
        return '-' * 30 + f'\nNumber [{phone}] has been deleted from [{name}]\n' + '-' * 30
    elif phone == '':
        confirmation = input(f'Do you want to delete contact {name} completely? Y/N: ')
        if confirmation.lower() == 'y':
            book.del_record(name)
            return '-' * 30 + f'\nContact [{name}] has been deleted!!!\n' + '-' * 30
        else:
            return '-' * 30 + f'\nContinue...\n' + '-' * 30


def info_funk() -> str:
    return '=' * 30 + '\nMain commands:\n'\
                     'add - add new contact\\contact number\n'\
                     'change - change contact number\n'\
                     'del - delete contact\\number\n'\
                     'phone - number search by name\n'\
                     'show all - show all contacts\n' + '=' * 30


@input_error
def search_func(name: str) -> str:
    """Displays the phone number for the specified name."""

    name = name.strip().title()
    if name in book.data.keys():
        contact = book.data[name]
        phones = contact.get_all_numbers()

        return '-' * 30 + f'\n[{name}]:{phones}\n' + '-' * 30
    else:
        return '-' * 30 + '\nNo such contact found!\n' + '-' * 30


def show_all() -> str:
    """Displays the entire phonebook."""

    result = f'{"=" * 30}\n'

    phone_book = book.get_all_contacts()

    for contact in phone_book:
        for name in contact:
            result += f'{"-" * 15}\n' + f'{name}:\n'
            for number in contact[name]:
                result += '{:<15}|\n'.format(number)

    return result + f'{"=" * 30}\n'


def split_data(data: str) -> (str, str):
    """Distribution of data by name and phone"""

    s_data = data.strip().split(' ')
    name = s_data[0].title()
    if len(s_data) == 2:
        phone = s_data[1]
        if name.isnumeric():
            raise ValueError('Wrong name!')
        elif not phone.isnumeric():
            raise ValueError('Wrong phone!')
        return name, phone
    else:
        phone = ''
        return name, phone


OPERATIONS = {'hello': hello_func,
              'hi': hello_func,
              'add': add_func,
              'change': change_func,
              'del': del_funk,
              'info': info_funk,
              'phone': search_func,
              'show all': show_all
              }

stop_list = ('good bye', 'close', 'exit', 'bye', 'end', 'stop')

if __name__ == '__main__':
    book = AddressBook()
    main()
