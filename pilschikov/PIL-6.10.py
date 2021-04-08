#   -----------------------------------------------------------
#
#  напечатать таблицу следующего вида
#  100...00
#  020...00
#   ....
#  000...09
#
#   Copyright (c) 2021. Danil Smirnov
#   Released under GNU Public License (GPL)
#   email zabanen.nu@ya.ru
#   -----------------------------------------------------------

for i in range(1, 10):
    table = '0' * 9
    table = table[:i - 1] + str(i) + table[i:]
    print(table)
