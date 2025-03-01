"""
У вас є текстовий файл, який містить інформацію про місячні заробітні
плати розробників у вашій компанії. Кожен рядок у файлі містить
прізвище розробника та його заробітну плату, які розділені комою без пробілів.

Наприклад:
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000

Ваше завдання - розробити функцію total_salary(path), яка аналізує цей
файл і повертає загальну та середню суму заробітної плати всіх розробників.
"""

import os


def total_salary(path):
    money_list = []
    with open(path, mode="r", encoding="utf-8") as file:
        for line in file.readlines():
            money = float(line.strip().split(",")[-1])
            money_list.append(money)
    return (sum(money_list), sum(money_list) / len(money_list))


fname = "./in/salary_file.txt"
if os.path.isfile(fname):
    total, average = total_salary(fname)
    print(
        f"Загальна сума заробітної плати: {total:.2f}, Середня заробітна плата: {average:.2f}"
    )
else:
    print(f"File '{fname}' not found...")
