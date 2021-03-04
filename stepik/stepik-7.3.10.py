#  Copyright (c) 2021. by Danil Smirnov
#  zabanen.nu@ya.ru
#  program calculates sum of divisors of n
number = int(input())
total = 0
for divisor in range(1, number + 1):
    if number % divisor == 0:
        total += divisor
print(total)
