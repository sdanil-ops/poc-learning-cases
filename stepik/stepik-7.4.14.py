#  Copyright (c) 2021. by Danil Smirnov
#  zabanen.nu@ya.ru
#  The input to the program is an integer, the cost of anything.
#  The program calculates the minimum number of coins with denominations of 1, 5, 10, 25
pay_count = int(input())
total_coins = 0
while pay_count != 0:
    if pay_count >= 25:
        total_coins += pay_count // 25
        pay_count = pay_count % 25
    elif pay_count >= 10:
        total_coins += pay_count // 10
        pay_count = pay_count % 10
    elif pay_count >= 5:
        total_coins += pay_count // 5
        pay_count = pay_count % 5
    elif pay_count >= 1:
        total_coins += pay_count // 1
        pay_count = 0

print(total_coins)
