#   -----------------------------------------------------------
#
#   вычислить y= √3+(√6..+(√96+√99))
#
#   Copyright (c) 2021. Danil Smirnov
#   Released under GNU Public License (GPL)
#   email zabanen.nu@ya.ru
#   -----------------------------------------------------------
for i in range(99, 0, -3):
    y = i ** 0.5 + (i + 1) ** 0.5

print(y)
