#  Copyright (c) 2021. by Danil Smirnov
#  zabanen.nu@ya.ru
#  read a sequence of 10 integers and determine whether each of them is even or not
flag = True

for i in range(10):
    n = int(input())
    if n % 2 != 0:
        flag = False
print('YES' if flag else 'NO')
