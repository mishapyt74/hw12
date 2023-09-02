import datetime

class Birthday:
    def __init__(self, day, month):
        self.day = day
        self.month = month

class Field:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.validate(value)
        self.value = value

    def validate(self, value):
        pass

class Phone(Field):
    def validate(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be a 10-digit number")

class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = name
        self.phone = phone
        self.birthday = birthday

    def days_to_birthday(self):
        if not self.birthday:
            return None
        today = datetime.date.today()
        next_birthday = datetime.date(today.year, self.birthday.month, self.birthday.day)
        if today > next_birthday:
            next_birthday = datetime.date(today.year + 1, self.birthday.month, self.birthday.day)
        days_remaining = (next_birthday - today).days
        return days_remaining

class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def remove_record(self, record):
        self.records.remove(record)

    def iterator(self, batch_size):
        for i in range(0, len(self.records), batch_size):
            yield self.records[i:i+batch_size]

birthday1 = Birthday(15, 8)
record1 = Record("Pasha Cucumber", "4141616262", birthday1)

birthday2 = Birthday(9, 12)
record2 = Record("Tony Stark", "380935212411", birthday2)

address_book = AddressBook()
address_book.add_record(record1)
address_book.add_record(record2)
