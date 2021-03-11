#  Copyright (c) 2021. by Danil Smirnov
#  zabanen.nu@ya.ru
#  The program will determine if the input number contains the same digits

def number_separator(num: int):
    # splits number into digits
    if num < 0:
        num = abs(num)
    while num != 0:
        last_digit = num % 10
        num = num // 10
        number_list.append(last_digit)


def compare_numbers(numbers: list)->bool:
    # determine if there is same digits in number list
    for pos in range(len(numbers) - 1):
        flag = False
        for k in range(pos + 1, len(numbers)):
            if numbers[k] == numbers[pos]:
                flag = True
                return flag


number_list = []  # define a list of digits of the entered number
print('The program will determine if the number contains the same digits')
number_separator(int(input('Input your number:\n')))  # divide the entered number by digits
same = compare_numbers(number_list) # compare numbers
if len(number_list) >= 2: # user can also input one-digit number
    print('Include same numbers' if same else 'All numbers are different')
else:
    print('There is one digit')
