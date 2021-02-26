"""# fibonaccu

n = int(input())
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(1, n + 1):
    print(fibonacci(i), end=' ')

#a, b = b, a + b"""


f1 = f2 = 1

n = int(input())

if n < 2:
    print('1')
    quit()

print(f1, end=' ')
print(f2, end=' ')
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')

print()