"""
Напишіть консольного бота помічника, який розпізнаватиме команди, що
вводяться з клавіатури, та буде відповідати відповідно до введеної команди.

☝ Бот помічник повинен стати для нас прототипом застосунку-асистента, який
ми розробимо в наступних домашніх завданнях. Застосунок-асистент в першому
наближенні повинен вміти працювати з книгою контактів та календарем.
"""


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."


def show_phone(args, contacts):
    name, = args
    return contacts[name]


def show_all(contacts):
    for name in contacts.keys():
        print(f"{name}: {contacts[name]}")


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
            show_all(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
