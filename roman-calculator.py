#   -----------------------------------------------------------
#
#   roman calculator
#   supports 4 operations (+, -, *, /)
#
#   Copyright (c) 2021. Danil Smirnov
#   Released under GNU Public License (GPL)
#   email zabanen.nu@ya.ru
#   -----------------------------------------------------------

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


def get_roman(arabic):
    thousands = ['', 'M', 'MM', 'MMM', 'MMMM']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    th = thousands[arabic // 1000]
    hn = hundreds[arabic // 100 % 10]
    ts = tens[arabic // 10 % 10]
    on = ones[arabic % 10]

    return th + hn + ts + on


def calculate_roman(roman: str, operator: str, _roman: str)-> str:
    roman = get_arabic(roman)
    _roman = get_arabic(_roman)
    if operator == '+':
        return get_roman(roman + _roman)
    elif operator == '-':
        if get_roman(roman - _roman) == '':
            return 'N'
        if roman - _roman < 0:
            return f'-{get_roman(_roman - roman)}'
        return get_roman(roman - _roman)
    elif operator == '*':
        return get_roman(roman * _roman)
    elif operator == '/':
        return get_roman(roman // _roman)



try:
    while True:
        print('Result is:', calculate_roman(*input('Input an expression like MDXII + MDCVI\n').split()))
except KeyboardInterrupt:
    print('Closing')
