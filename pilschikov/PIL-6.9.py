#  Copyright (c) 2021. by Danil Smirnov
#  zabanen.nu@ya.ru
#  напечатать в одну строку все литеры между 'A' и 'Z'
#  включая и эти буквы

for i in range(ord('A'), ord('Z') + 1):
    print(chr(i), end='')
