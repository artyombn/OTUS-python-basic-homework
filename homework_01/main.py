"""
Домашнее задание №1
Функции и структуры данных
"""

#pytest testing/test_homework_01 -s -vv

def power_numbers(*numbers):
    return [i ** 2 for i in numbers]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def prime_test(number):                    #Функция, проверяющая простое число или нет
    k = 2                                  #Счетчик делениий
    if number <= 1:                        #Исключаем все значения <=1, которые не являются простыми числами
        return False
    else:
        while number % k != 0:             #Цикл для определения деления без остатка в диапазоне от k до заданного числа
            k += 1
        if k == number:                    #Если кол-во делений будет равно числу --> число простое
            return True
        else:
            return False                   #Деление без остатка произошло раньше, чем кол-во делений дошло до значения числа

def filter_numbers(number, filter):
    if filter == 'odd':
        return [i for i in number if i%2 != 0]
    elif filter == 'even':
        return [i for i in number if i%2 == 0]
    else:
        return [i for i in number if prime_test(i) == True]