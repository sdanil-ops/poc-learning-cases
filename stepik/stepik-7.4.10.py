#  Copyright (c) 2021. by Danil Smirnov
#  zabanen.nu@ya.ru
#  The input to the program is a sequence of integers divisible by 7, each number on a separate line.
#  The end of the sequence is any number not divisible by 7.
#  program displays the members of the given sequence.

number = int(input())
while number % 7 == 0:
    print(number)
    number = int(input())
