#  -----------------------------------------------------------
#
#  Pilschikov task 1.1
#  Write down next numbers (4 decimal places)
#  a) 5!, b) LXIV, c) 6.38
#  d) -0,7(4), e) 11/4, f) -1/6
#  g) √2, h) π, i) 5*10^6
#  j) -24.8*10^-7, k) 10^6, l) 1/100000
#
#  Copyright (c) 2021. Danil Smirnov
#  Released under GNU Public License (GPL)
#  email zabanen.nu@ya.ru
#  -----------------------------------------------------------
from math import pi


def get_arabic(roman: str) -> int:
    roman = roman.upper()
    roman_digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    previous = roman[-1]
    result = roman_digits[previous]
    for current in roman[-2::-1]:
        if roman_digits[current] >= roman_digits[previous]:
            result += roman_digits[current]
        else:
            result -= roman_digits[current]

        previous = current

    return result


def get_factorial(number: int) -> int:
    if number == 0:
        return 1
    return get_factorial(number - 1) * number


def get_periodic_fraction(number, period, decimal_places=4):
    number_storage = number
    while number % 1 !=0:
        number *= 10
    number = number_storage
    result = str(number) + str(period) * (decimal_places - 1)
    return result


def round_decimal_places(number, limit: int = 4) -> str:
    return f'{number:.{limit}f}'


task_list = {'a)': get_factorial(5), 'b)': get_arabic('lxiv'),
             'c)': 6.38, 'd)': get_periodic_fraction(-0.7, 4),
             'e)': 11 / 4, 'f)': round_decimal_places(-1 / 6),
             'g)': round_decimal_places(2 ** 0.5), 'h)': round_decimal_places(pi),
             'i)': 5 * 10 ** 6, 'j)': round_decimal_places(-24.8 * (10 ** -7)),
             'k)': 10 ** 6, 'l)': round_decimal_places(1 / 10000)
             }

for task in task_list:
    print(task, task_list[task])
