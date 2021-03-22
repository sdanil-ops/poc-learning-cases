#  Copyright (c) 2021. by Danil Smirnov
#  zabanen.nu@ya.ru
#  напечатать таблицу следующего вида
#  100...00
#  020...00
#   ....
#  000...09

for i in range(1, 10):
    table = '0' * 9
    table = table[:i - 1] + str(i) + table[i:]
    print(table)
