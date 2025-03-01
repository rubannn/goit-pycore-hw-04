"""
Розробіть скрипт, який приймає шлях до директорії в якості аргументу
командного рядка і візуалізує структуру цієї директорії, виводячи імена
всіх піддиректорій та файлів. Для кращого візуального сприйняття, імена
директорій та файлів мають відрізнятися за кольором.

Вимоги до завдання:
- Створіть віртуальне оточення Python для ізоляції залежностей проекту.
- Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях
вказує, де знаходиться директорія, структуру якої потрібно відобразити.
- Використання бібліотеки colorama для реалізації кольорового виведення.
- Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи
рекурсивний спосіб обходу директорій (можна, за бажанням, використати
не рекурсивний спосіб).
- Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях
не існує або він не веде до директорії.
"""

import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)
BLUE = Fore.BLUE
GREEN = Fore.GREEN


def dir_tree(dir_path: Path, depth=1):
    items = list(dir_path.iterdir())  # all childrens in dir
    
    for item in items:
        indent = "\t" * depth  # calc indents
        if item.is_dir():
            print(BLUE + f"{indent}{item.name}/")  # print folders +  `/`
            dir_tree(item, depth + 1)  # recursion call
        else:
            print(GREEN + f"{indent}{item.name}")  # print files


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use: python 03.py <dir_path>")
        sys.exit(1)

    dir_path = Path(sys.argv[1]).resolve()  # absolute path
    if not dir_path.is_dir():
        print("Path is not directory...")
        sys.exit(1)

    print(BLUE + dir_path.as_posix() + "/")
    dir_tree(dir_path)


# python 03.py 'd:\AP\'
