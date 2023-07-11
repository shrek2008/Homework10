from AdressBook import *

contacts = AdressBook()

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params"
    return inner

def hello(*args):
    return "How can I help you?"

@input_error
def add(*args):
    list_of_param = args[0].split()
    name_value = list_of_param[0]
    phone_values = list_of_param[1:]
    if not phone_values:
        raise IndexError("Not enough params")
    name = Name(name_value)
    phone_number = " ".join(phone_values)
    phone = Phone(phone_number)
    record = Record(name, phone)
    contacts.add_person(record)
    return f"Added {name_value}, phone:{phone_number}"

def exit(*args):
    return "Good bye!"

def no_command(*args):
    return "Write a person and phone"

def show_all(*args):
    return contacts

@input_error
def change(*args):
    list_of_param = args[0].split()
    name_value = list_of_param[0]
    phone_values = list_of_param[1:]
    if not phone_values:
        raise IndexError("Not enough params")
    name = Name(name_value)
    phone_number = " ".join(phone_values)
    phone = Phone(phone_number)
    record = Record(name, phone)
    if name_value in contacts:
        contacts[name_value].phones = [phone]
        return f"Changed {name_value}'s phone number to {phone_number}"
    else:
        return f"No contact found for {name_value}"

@input_error
def phone(phone_num):
    for name, numbers in contacts.items():
        if phone_num in numbers:
            return f"{name.title()}: {numbers[numbers.index(phone_num)]}"
    return "No contact found"

def help(*args):
    return "To add someone write add *Name* *phone*\nTo change write change and name and phone\nTo phone write a number\nTo show all write show_all"

COMMANDS = {hello: "hello",
            add: "add",
            change: "change",
            exit: "exit",
            show_all: "show_all",
            phone: "phone",
            help: "help"}

def command_handler(text):
    text = text.lower()
    if text in ['goodbye', 'close', 'exit']:
        return exit, None
    for command, k_word in COMMANDS.items():
        if text.startswith(k_word):
            data = text.replace(k_word, '').strip()
            if command == phone:
                return command, data.title()
            else:
                return command, data
    return no_command, None



def main():
    print(hello())
    while True:
        input_var = input(">>>")
        command, data = command_handler(input_var)
        print(command(data))
        if command == exit:
            break

if __name__ == "__main__":
    main()
