#  -----------------------------------------------------------
#  Euclidean algorithm for computing the greater common divisor
#  of two numbers
#
#  Copyright (c) 2021. Danil Smirnov
#  Released under GNU Public License (GPL)
#  email zabanen.nu@ya.ru
#  -----------------------------------------------------------

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print('This program calculates greater common divisor of two numbers')
a, b = int(input('Input first number: \n')), int(input('Input second number: \n'))
print( 'Greater common divisor is: ',gcd(a, b))
