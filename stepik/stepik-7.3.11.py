# program for calculating the alternating sum of n
n = int(input())
x = 0
for i in range(1, n +1):
    if i % 2 == 0:
        x -= i
    else:
        x += i
print(x)