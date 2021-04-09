#   -----------------------------------------------------------
#
#   Pilschikov 5.16
#   Числа Фибоначчи f(n)
#   а) определить f(40)-е число Фибоначчи
#   b) найти f- первое число Фибоначчи большее m (m > 1)
#   с) вычислить сумму всех чисел Фибоначчи не превышающих 1000
#
#   Copyright (c) 2021. Danil Smirnov
#   Released under GNU Public License (GPL)
#   email zabanen.nu@ya.ru
#   -----------------------------------------------------------
fibonacci = {0: 0, 1: 1}

def fib(n=40):
    if n in fibonacci:
        return fibonacci[n]
    fibonacci[n] = fib(n - 1) + fib(n - 2)
    return fibonacci[n]

def get_next_fib(m=100000000000000000):
    n = 0
    while fib(n) < m:
        n += 1
    return fib(n)

def get_fib_sum(max_fib=1000):
    result = 0
    n = 0
    while fib(n) <= max_fib:
        result += fib(n)
        n += 1
    return result



print('a)',fib())
print('b) При (m = 100)', get_next_fib())
print('c)', get_fib_sum())


