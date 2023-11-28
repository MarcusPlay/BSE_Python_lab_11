#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона;
# дата рождения (список из трех чисел). Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть размещены по алфавиту; вывод на экран информации о людях, чьи
# дни рождения приходятся на месяц, значение которого введено с клавиатуры; если таких
# нет, выдать на дисплей соответствующее сообщение.

def add_user(users):
    name = input('Введите Фамилию и Имя: ')
    phone_number = input('Введите Номер телефона: ')
    year = list(map(int, input('Введите дату рождения (пример: 05 07 2004): ').split()))

    user = {
        'name': name,
        'phone_number': phone_number,
        'year': year,
    }

    users.append(user)

    if len(users) > 1:
        users.sort(key=lambda item: item.get('name', ''))


def list_users(users):
    print('Введите число месяца (1 - 12): ')
    while True:
        num = int(input())
        if num < 1 or num > 12:
            print("Значение введено неправильно! Попробуйте еще раз.")
        else:
            break
    
    line = '+-{}-+-{}-+-{}-+-{}-+'.format('-' * 4, '-' * 20, '-' * 18, '-' * 10)
    print(line)
    print('| {:^4} | {:^20} | {:^18} | {:^10} |'.format(
        "№", 
        "Название", 
        "Номер телефона", 
        "Дата"
            )
        )
    print(line)

    for idx, user in enumerate(users, 1):
        if user['year'][1] == num:
            print(
                '| {:^4} | {:^20} | {:^18} | {:^10} |'.format(
                    idx, 
                    user['name'], 
                    user['phone_number'], 
                    ' '.join(map(str, user['year']))
                        )
                    )
            print(line)


if __name__ == "__main__":
    users = []

    while True:
        command = input("~<| ").lower()

        match command:
            case 'exit':
                break

            case 'add':
                add_user(users)

            case 'list':
                list_users(users)
