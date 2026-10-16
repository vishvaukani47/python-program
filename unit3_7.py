#Practical: Write a program that moves all zeros in a list to the end, while keeping the order of non-zero elements the same.

nums = [0, 1, 0, 3, 12]
result = []
for num in nums:
    if num != 0:
        result.append(num)
for num in nums:
    if num == 0:
        result.append(num)

print(result)

