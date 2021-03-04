#  Copyright (c) 2021. by Danil Smirnov
#  zabanen.nu@ya.ru
#  Write a program that calculates the sum of those numbers from 1 to n (inclusive)
#  whose square ends in 2, 5 or 8

number = int(input())
counter = 0
for i in range(1, number + 1):
    if i % 10 == 5:  # scuare of any number cannot ends with 2 or 8
        counter += i

print(counter)
