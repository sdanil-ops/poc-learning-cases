#  Copyright (c) 2021. by Danil Smirnov
#  zabanen.nu@ya.ru
#  program for calculating the alternating sum of numbers
number = int(input())
sum_of_numbers = 0
for i in range(1, number + 1):
    if i % 2 == 0:
        sum_of_numbers -= i
    else:
        sum_of_numbers += i
print(sum_of_numbers)
