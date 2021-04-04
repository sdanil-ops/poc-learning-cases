#  -----------------------------------------------------------
#
#  write a program that prints true or false depending
#  on whether the given three integers have the same parity
#
#  Copyright (c) 2021. Danil Smirnov
#  Released under GNU Public License (GPL)
#  email zabanen.nu@ya.ru
#  -----------------------------------------------------------
even = 0
add = 0

for i in range(1, 4):
    n = int(input(f'Input №{i} digit:\n'))
    if n % 2 == 0:
        even += n
    else:
        add += n

print('true' if (even != 0 or add != 0) and (add == 0 or even == 0) else 'false' )
