from support_functions import split_data, check_date, phone_valid
from datetime import datetime
from BookClasses import AddressBook, Record
import pickle


def main():
    """Main function"""

    print('=' * 30 + '\nMain commands:\n'
                     'new book - create a new book\n'
                     'load book - load the book\n'
                     'save book - save the book\n'
                     'add - add new contact\\contact number\n'
                     'birthday - add birthday to contact (dd.mm.yyyy)\n'
                     'change - change contact number\n'
                     'del - delete contact\\number\n'
                     'phone - number search by name\n'
                     'show all - show all contacts\n'
                     'when birthday - remaining days until the birthday\n'
                     'info - command information\n' + '=' * 30)
    while True:
        input_command = input('Enter command: ')

        if input_command.lower() in STOP_LIST:
            if input('Do you want to save the book? Y/N: ').upper() == 'Y':
                save_book()
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
        except ValueError:
            return '-' * 75 + '\nInvalid name, number or date!\n' \
                              'The name must start with a letter.\n' \
                              'The number must be between 10 and 13 characters long.\n' \
                              'Sample number: 0671234567 or +380671234567\n' \
                              'Sample number: 01.01.2001 or 2001-01-01\n' + '-' * 75
        except (IndexError, KeyError, TypeError, AttributeError):
            return '-' * 75 + '\nPlease check the command you entered!\n' \
                              'The "add" and "change" commands accept two parameters each ' \
                              '(name and number).\n' \
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
            data = input_command[len(command):].strip()
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

    if name not in my_book.data.keys() and phone:
        new_contact = Record(name, phone)
        my_book.add_record(new_contact)
        return '-' * 30 + f'\nNew contact has been added:\n[{name}]:[{phone}]\n' + '-' * 30
    elif name not in my_book.data.keys() and not phone:
        new_contact = Record(name)
        my_book.add_record(new_contact)
        return '-' * 30 + f'\nNew contact has been added:\n[{name}]\n' + '-' * 30

    contact = my_book.data[name]
    if not contact.phone_in_contact(phone) and phone:
        for number in contact.get_all_numbers():
            if number == 'There are no phone numbers.':
                contact.del_phone(number)
        contact.add_phone(phone)
        return '-' * 30 + f'\nNumber [{phone}] has been added to contact: [{name}]\n' + '-' * 30
    elif contact.phone_in_contact(phone):
        return '-' * 30 + '\nSuch a phone number already exists!\n' + '-' * 30
    else:
        return '-' * 30 + '\nSuch a contact already exists!\n' + '-' * 30


def add_birthday(data: str) -> str:
    s_data = data.strip().split(' ')
    name = s_data[0]
    name = name.strip().title()
    b_date = s_data[1]
    s_date = check_date(b_date)
    if not s_date:
        return '-' * 30 + '\nInvalid date!\n' + '-' * 30
    if name in my_book.data.keys():
        contact = my_book.data[name]
        s_date = datetime.strptime(s_date, '%Y-%m-%d').date()
        contact.birthday = s_date

        return '-' * 30 + f'\nBirthday has been added [{name}]:[{s_date}]\n' + '-' * 30
    else:
        return '-' * 30 + '\nNo such contact found!\n' + '-' * 30


@input_error
def change_func(data: str) -> str:
    """Replaces a contact in the phone book."""

    name, phone_old = split_data(data)

    if name in my_book.data.keys():
        contact = my_book.data[name]
        if contact.phone_in_contact(phone_old):
            phone_new = input('Please enter a new number: ')
            phone_new = phone_valid(phone_new)
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
    if name not in my_book.data.keys():
        return '-' * 30 + f'\nContact with name {name} not found!\n' + '-' * 30
    contact = my_book.data[name]
    if contact.phone_in_contact(phone):
        contact.del_phone(phone)
        return '-' * 30 + f'\nNumber [{phone}] has been deleted from [{name}]\n' + '-' * 30
    elif phone == '':
        confirmation = input(f'Do you want to delete contact {name} completely? Y/N: ')
        if confirmation.lower() == 'y':
            my_book.del_record(name)
            return '-' * 30 + f'\nContact [{name}] has been deleted!!!\n' + '-' * 30
        else:
            return '-' * 30 + f'\nContinue...\n' + '-' * 30


def info_funk() -> str:
    return '=' * 30 + '\nMain commands:\n' \
                     'new book - create a new book\n' \
                     'load book - load the book\n' \
                     'save book - save the book\n' \
                     'add - add new contact\\contact number\n'\
                     'birthday - add birthday to contact (dd.mm.yyyy)\n'\
                     'change - change contact number\n'\
                     'del - delete contact\\number\n'\
                     'phone - number search by name\n'\
                     'show all - show all contacts\n'\
                     'when birthday - remaining days until the birthday\n' + '=' * 30


@input_error
def search_func(name: str) -> str:
    """Displays the phone number for the specified name."""

    name = name.strip().title()
    return my_book.find_contact(name)


def show_all() -> str:
    """Displays the entire phonebook."""

    print('=' * 30)
    result = ''

    phone_book = my_book.get_all_contacts()

    for contact in phone_book:
        for name in contact:
            result += f'{"-" * 15}\n' + f'{name}:\n'
            for number in contact[name]:
                result += '{:<15}|\n'.format(number)

    if result:
        return result + f'{"=" * 30}\n'
    else:
        return 'The book is empty.\n' + "=" * 30


def when_birthday(name: str) -> str:
    name = name.strip().title()
    if name in my_book.data.keys():
        contact = my_book.data[name]
        difference = contact.days_to_birthday()
        if isinstance(difference, str):
            return difference
        return '-' * 30 + f'\n{name} birthday, after {difference} days.\n' + '-' * 30
    else:
        return '-' * 30 + '\nNo such contact found!\n' + '-' * 30


def new_book() -> str:
    global my_book
    my_book = AddressBook()
    print('-' * 30)
    book_name = input('Enter new book name: ')
    print(f'\n{"=" * 30}\n')

    my_book.change_book_name(book_name)
    return f'A new book [{book_name}] has been created.'


def load_book() -> str:
    try:
        with open('saved_books.txt', 'r') as fh:
            book_list = fh.readlines()
            print('-' * 30 + '\nSaved books:')
            for book in book_list:
                print(book, end='')
    except FileNotFoundError:
        print('-' * 30 + '\nSaved books not found.\n' + '-' * 30)
        new_book_yn = input('Do you want to create a new book? Y/N: ')
        if new_book_yn.upper() == 'Y':
            return new_book()
        else:
            return '-' * 30 + '\nCancel load.\n' + '-' * 30

    book_file = input('-' * 30 + '\nEnter book name: ')
    try:
        with open(book_file + '.dat', 'rb') as fh:
            global my_book
            my_book = pickle.load(fh)
            return '-' * 30 + f'\nThe book [{my_book.book_name}] has been loaded.\n' + '-' * 30
    except FileNotFoundError:
        return '-' * 30 + '\nFile not found.\n' + '-' * 30


def save_book() -> str:

    if not my_book.book_name:
        print('-' * 30 + '\nThis is a new book.')
        my_book.book_name = input('Please enter new book name: ')
        print('-' * 30)

    with open(my_book.book_name + '.dat', 'wb') as fh:
        pickle.dump(my_book, fh)

    with open('saved_books.txt', 'r') as file_r:
        books_list = file_r.readlines()

        if f'{my_book.book_name}\n' not in books_list:

            with open('saved_books.txt', 'a') as file_a:
                file_a.write(f'{my_book.book_name}\n')

    return '-' * 30 + f'\nThe book [{my_book.book_name}] was saved.\n' + '-' * 30


def the_searcher(data: str):
    name = None
    phone = None
    result = []
    if data[0].isalpha():
        name = data.strip().lower()
    elif data[0].isdigit() or data[0] == '+':
        phone = data
    else:
        raise ValueError('Unknown data')

    if name:
        with open('saved_books.txt', 'r') as file_r:
            for book in file_r.readlines():
                with open(book.strip() + '.dat', 'rb') as file_rb:
                    search_book = pickle.load(file_rb)
                    for contact in search_book.data:
                        if name in contact.lower():
                            result.append(search_book.find_contact(contact))
    elif phone:
        with open('saved_books.txt', 'r') as file_r:
            for book in file_r.readlines():
                with open(book.strip() + '.dat', 'rb') as file_rb:
                    search_book = pickle.load(file_rb)
                    for contact in search_book.get_all_contacts():
                        for numbers in contact.values():
                            for number in numbers:
                                if phone in number and contact not in result:
                                    result.append(contact)

    for i in result:
        print(i)

    return '-' * 30


OPERATIONS = {'hello': hello_func,
              'hi': hello_func,
              'add': add_func,
              'birthday': add_birthday,
              'change': change_func,
              'del': del_funk,
              'info': info_funk,
              'phone': search_func,
              'find': the_searcher,
              'show all': show_all,
              'when birthday': when_birthday,
              'new book': new_book,
              'load book': load_book,
              'save book': save_book
              }

STOP_LIST = ('good bye',
             'close',
             'exit',
             'bye',
             'end',
             'stop',
             'break'
             )

if __name__ == '__main__':

    my_book = AddressBook()

    main()
