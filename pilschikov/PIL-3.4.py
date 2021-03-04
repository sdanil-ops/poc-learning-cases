# task 3.4 page 14
even = 0
add = 0

for i in range(3):
    n = int(input())
    if n % 2 == 0:
        even += n
    else:
        add += n

print('true' if (even != 0 or add != 0) and (add == 0 or even == 0) else 'false' )
