#Practical3: Write a Python program to display element of list in reverse order using loops.
lst = [10, 20, 30, 40, 50]
print("Original List:", lst)
print("List in Reverse Order:")
for i in range(len(lst) - 1, -1, -1):
    print(lst[i])
