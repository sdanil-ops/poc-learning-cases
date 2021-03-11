#  -----------------------------------------------------------
#  Task 5.44
#
#  Count how many numbers are greater than the adjacent numbers
#
#  Copyright (c) 2021. Danil Smirnov
#  Released under GNU Public License (GPL)
#  email zabanen.nu@ya.ru
#  -----------------------------------------------------------


def counter(numbers_list: list):
    '''counter how many numbers in list are greater than the adjacent numbers'''
    count = 0
    quantity_numbers = len(numbers_list)
    for i in range(quantity_numbers):
        if numbers_list[i - 1] < numbers_list[i] and numbers_list[i + 1] < numbers_list[i]:
            count += 1
    return count


def counter_test(count):   # that func shows that all works as planed
    '''preventive testing'''
    print('Testing', counter.__doc__)
    print('Testcase #1:', end=' ')
    numbers_list = [1, 2, 1, 44, 5, 1, 0]
    answer = 2
    count(numbers_list)
    print('Passed!' if count(numbers_list) == answer else 'Fail')

    print('Testcase #2:', end=' ')
    numbers_list = [1, 2, 1, 44, 5, 6, 0, 1, 0, 2, 5, 99, 1]
    answer = 5
    count(numbers_list)
    print('Passed!' if count(numbers_list) == answer else 'Fail')

    print('Testcase #3:', end=' ')
    numbers_list = [0, 0, 0, 0, 0, 0, 0]
    answer = 0
    count(numbers_list)
    print('Passed!' if count(numbers_list) == answer else 'Fail')

counter_test(counter)