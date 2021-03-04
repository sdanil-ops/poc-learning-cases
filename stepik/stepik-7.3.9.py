#  Copyright (c) 2021. by Danil Smirnov
#  zabanen.nu@ya.ru
#  a program that reads 10 numbers and outputs multiplication of nonzero numbers
counter = 1

for i in range(10):
    num = int(input())
    if num != 0:
        counter *= num
print(counter)
