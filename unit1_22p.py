#22. find a sum of 15 + 25 +………+n5.

n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total = total + i ** 5

print("Sum of series =", total)