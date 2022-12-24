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

def is_prime(number):                      #Функция, проверяющая простое число или нет
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


#До того, как прочитал про реализацию через filter()
#----------------------------------------------------------
# def filter_numbers(number, filter_type):
#     if filter_type == ODD:
#         return [i for i in number if i%2 != 0]
#     elif filter_type == EVEN:
#         return [i for i in number if i%2 == 0]
#     else:
#         return [i for i in number if is_prime(i)]
#----------------------------------------------------------

def filter_numbers(number, filter_type):
    if filter_type == ODD:
        return list(filter(lambda x: x%2 != 0, number))
    elif filter_type == EVEN:
        return list(filter(lambda x: x%2 == 0, number))
    else:
        return list(filter(lambda x: is_prime(x), number))