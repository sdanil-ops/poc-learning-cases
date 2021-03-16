#  -----------------------------------------------------------
#  дано натуральное k. Определить k-ю цифру в последовательности
#  1101001000100001000001000000...
#  в которой выписаны подряд все степени 10
# 
#  Copyright (c) 2021. Danil Smirnov
#  Released under GNU Public License (GPL)
#  email zabanen.nu@ya.ru
#  -----------------------------------------------------------

k = int(input('Введите целое число\n'))
sequence = '1'
for i in range(1, k):
    sequence += str(10 ** i)

print(sequence[k])
