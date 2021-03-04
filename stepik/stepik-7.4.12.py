#  Copyright (c) 2021. by Danil Smirnov
#  zabanen.nu@ya.ru
#  The program input is a sequence of integers from one to five
#  characterizing the student's assessment, each number per individual.
#  The constructor shows any negative number, or a number greater five
#  Write a program that prints the number of fives.

total_fives = 0
number = int(input())

while 0 <= number <= 5:
    number = int(input())
    if number == 5:
        total_fives += 1
print(total_fives)
