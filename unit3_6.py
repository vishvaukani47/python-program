#Practical6 : Write a program to remove all occurrences of a given element from a list. Input:

nums = [1, 2, 3, 2, 4, 2, 5]
element = 2
result = []
for num in nums:
    if num != element:
        result.append(num)

print(result)
