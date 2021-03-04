#  Copyright (c) 2021. by Danil Smirnov
#  zabanen.nu@ya.ru
#  a program that reads a natural number
#  and prints the first n numbers of the Fibonacci sequence.
first_fibonacci = second_fibonacci = 1

number = int(input())

if number < 2:
    print('1')
    quit()

print(first_fibonacci, end=' ')
print(second_fibonacci, end=' ')
for i in range(2, number):
    first_fibonacci, second_fibonacci = second_fibonacci, first_fibonacci + second_fibonacci
    print(second_fibonacci, end=' ')
