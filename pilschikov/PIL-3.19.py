#  -----------------------------------------------------------
#  The program will determine if the input number contains the same digits
#
#  Copyright (c) 2021. Danil Smirnov
#  Released under GNU Public License (GPL)
#  email zabanen.nu@ya.ru
#  -----------------------------------------------------------

def number_separator(num: int):
    # splits number into digits
    if num < 0:
        num = abs(num)
    while num != 0:
        last_digit = num % 10
        num = num // 10
        number_list.append(last_digit)


def compare_numbers(numbers: list) -> bool:
    # determine if there is same digits in number list
    for pos in range(len(numbers) - 1):
        for k in range(pos + 1, len(numbers)):
            if numbers[k] == numbers[pos]:
                flag = True
                return flag


number_list = []  # define a list of digits of the entered number
print('The program will determine if the number contains the same digits')
number = input('Input your number:\n').replace('.', '')

try:
    number_separator(int(number))
    same = compare_numbers(number_list)  # compare numbers

    if len(number_list) >= 2:  # user can also input one-digit number
        print('Include same numbers' if same else 'All numbers are different')
    else:
        print('There is one digit')
except ValueError:
    number = input("You've input string, please input number:\n").replace('.', '')
    number_separator(int(number))
    same = compare_numbers(number_list)  # compare numbers

    if len(number_list) >= 2:  # user can also input one-digit number
        print('Include same numbers' if same else 'All numbers are different')
    else:
        print('There is one digit')
