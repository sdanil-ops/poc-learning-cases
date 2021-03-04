#  Copyright (c) 2021. by Danil Smirnov
#  zabanen.nu@ya.ru
#  a program that prints the largest and
#  second largest number of a sequence of numbers entered
iterations_quantity = int(input())
first_num = 0
second_num = 0

for i in range(iterations_quantity):
    number = int(input())
    if number > first_num:
        second_num = first_num
        first_num = number
    else:
        if first_num > number > second_num:
            second_num = number

print(first_num)
print(second_num)
