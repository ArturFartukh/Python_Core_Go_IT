from collections import UserDict
from datetime import date


class AddressBook(UserDict):
    """Class AddressBook """
    # index = 0
    # step = 5
    #
    # def __next__(self):
    #     if self.index < len(self.data):
    #         result = []
    #         for contact in self.data:
    #             result.append(contact)
    #             self.index += 1
    #             if self.index == self.step:
    #                 return result
    #         if result:
    #             return result
    #     raise StopIteration

    def add_record(self, record):
        self.data[record.contact.value] = record

    def del_record(self, name):
        del self.data[name]

    def iterator(self, count=5):
        page = []
        i = 0
        for record in self.data.values():
            page.append(record)
            i += 1
            if i == count:
                yield page
                page = []
                i = 0
        if page:
            yield page

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
            phone = ''
        self.contact = Name(new_name)
        self.phones = [Phone(phone)]
        self.birthday = None

    def add_phone(self, new_phone: str):
        self.phones.append(Phone(new_phone))

    def birthday(self, birth_date):
        self.birthday = Birthday(birth_date)

    def change_phone(self, old: str, new: str):
        for number in self.phones:
            if number.value == old:
                number.value = new

    def days_to_birthday(self):
        if not self.birthday:
            return f'Date of birth not specified.'
        bd_in_year = self.birthday
        bd_in_year = bd_in_year.replace(year=date.today().year)
        if bd_in_year > date.today():
            difference = bd_in_year - date.today()
            return difference.days
        elif bd_in_year < date.today():
            difference = bd_in_year.replace(year=date.today().year + 1) - date.today()
            return difference.days
        else:
            return 'Happy Birthday!'

    def del_phone(self, del_phone):
        for number in self.phones:
            if number == del_phone:
                self.phones.remove(number)

    def get_all_numbers(self) -> list:
        return [number.value for number in self.phones]

    def phone_in_contact(self, phone) -> bool:
        for number in self.phones:
            if number.value == phone:
                return True
        return False


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    """Name field"""
    pass


class Phone(Field):
    """Phone field"""
    @Field.value.setter
    def value(self, value):
        if not len(value) == 13 and not value[0] == '+' and not value[1:].isdigit():
            raise ValueError('Invalid phone number.')
        self._value = value


class Birthday(Field):
    """Birthday field"""
    @Field.value.setter
    def value(self, value):
        if value > date.today():
            raise ValueError("Birthday must be less than current year and date.")
        self._value = value
