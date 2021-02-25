# input is natural number n. write program that computes n!
n = int(input())

def factorial(n):
    if n == 0:
        return 1
    f = 1
    i = 0

    while i < n:
        i += 1
        f *= i
    return f
print(factorial(n))
