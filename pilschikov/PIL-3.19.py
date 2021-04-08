#  -----------------------------------------------------------
#  The program will determine if the input number contains the same digits
#
#  Copyright (c) 2021. Danil Smirnov
#  Released under GNU Public License (GPL)
#  email zabanen.nu@ya.ru
#  -----------------------------------------------------------

def get_digits_list(_number: int):
    # splits number into digits
    number_list = []
    if _number < 0:
        _number = abs(_number)
    while _number != 0:
        last_digit = _number % 10
        _number = _number // 10
        number_list.append(last_digit)
    return number_list


def compare_numbers(numbers: list) -> bool:
    # determine if there is same digits in number list
    for pos in range(len(numbers) - 1):
        for k in range(pos + 1, len(numbers)):
            if numbers[k] == numbers[pos]:
                return True
    return False


print('The program will determine if the number contains the same digits')
number = input('Input your number:\n').replace('.', '')

try:
    same = compare_numbers(get_digits_list(int(number)))
    not_single_digit = len(get_digits_list(int(number))) >= 2
    if not_single_digit:
        print('Include same numbers' if same else 'All numbers are different')
    else:
        print('There is one digit')

except ValueError:
    print("You've input string")
