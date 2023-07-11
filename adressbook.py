from collections import UserDict

class AdressBook(UserDict):
    def add_person(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, name, phone=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone):
        self.phones.append(phone)

    def change_phone(self, new_phone):
        self.phone = new_phone



class Field:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value

    def __str__(self) -> str:
        return self.value


class Name(Field):
    pass

class Phone(Field):
    pass

if __name__ == "__main__":
    
    ad = AdressBook()
    name = Name("Boris")
    phone = Phone("+380681486757")
    person1 = Record(name, phone)

    print(f"{name}: {phone}")

    person1.add_phone(phone)

    person2 = Record(Name("Audi"), Phone("+30712"))
    
    ad.add_person(person1)
    ad.add_person(person2)
    print(ad)