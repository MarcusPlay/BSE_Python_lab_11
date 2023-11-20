#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Напишите функцию, которая считывает с клавиатуры числа и перемножает их до тех пор, пока не будет введен 0.
# Функция должна возвращать полученное произведение. Вызовите функцию и выведите на экран результат ее работы.

def multiply_until_zero():
    product = 1
    while True:
        num = int(input("Введите число (для завершения введите 0): "))
        if num == 0:
            break
        product *= num
    return product


if __name__=="__main__":
    result = multiply_until_zero()
    print(f"Результат перемножения: {result}")