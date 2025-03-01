"""
У вас є текстовий файл, який містить інформацію про котів. Кожен рядок
файлу містить унікальний ідентифікатор кота, його ім'я та вік,
розділені комою. Наприклад:

60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5

Ваше завдання - розробити функцію get_cats_info(path), яка читає
цей файл та повертає список словників з інформацією про кожного кота.
"""

import os


def get_cats_info(path):
    result = []
    with open(path, mode="r", encoding="utf-8") as file:
        for line in file.readlines():
            id, name, age = line.strip().split(",")
            result.append({"id": id, "name": name, "age": age})
    return result


if __name__ == "__main__":
    fname = "./in/cats_file.txt"
    if os.path.isfile(fname):
        cats_info = get_cats_info(fname)
        print(cats_info)
    else:
        print(f"File '{fname}' not found...")
