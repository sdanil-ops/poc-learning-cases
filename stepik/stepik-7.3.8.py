#  Copyright (c) 2021. by Danil Smirnov
#  zabanen.nu@ya.ru
# input is natural number n. write program that computes n!

number = int(input())


def factorial(num):
    if num == 0:
        return 1
    factorial = 1
    i = 0

    while i < num:
        i += 1
        factorial *= i
    return factorial


print(factorial(number))
