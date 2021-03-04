#  Copyright (c) 2021. by Danil Smirnov
#  zabanen.nu@ya.ru
#  program calculates sum of inputs while they positive

number = int(input())
total_positive_numbers = 0
while number >= 0:
    total_positive_numbers += number
    number = int(input())
print(total_positive_numbers)
