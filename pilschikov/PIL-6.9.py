#   -----------------------------------------------------------
#
#  напечатать в одну строку все литеры между 'A' и 'Z'
#  включая и эти буквы
#
#   Copyright (c) 2021. Danil Smirnov
#   Released under GNU Public License (GPL)
#   email zabanen.nu@ya.ru
#   -----------------------------------------------------------

for i in range(ord('A'), ord('Z') + 1):
    print(chr(i), end='')
