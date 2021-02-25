# Write a program that calculates the sum of those numbers from 1 to n (inclusive)
# whose square ends in 2, 5 or 8

n = int(input())
counter = 0
for i in range(1, n + 1):
    if i % 10 == 5: # scuare of any number cannot ends with 2 or 8
        counter += i

print(counter)
