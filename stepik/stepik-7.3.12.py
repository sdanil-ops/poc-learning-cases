#
n = int(input())
first_num = 0
second_num = 0

for i in range(n):
    x = int(input())
    if x > first_num:
        second_num = first_num
        first_num = x
    else:
        if x < first_num  and  x > second_num:
            second_num = x

print(first_num)
print(second_num)