#Practical1 : Write a program to remove all duplicate elements in a list.
lst = [10, 20, 10, 30, 20, 40, 30]
new_list = []
for i in lst:
    if i not in new_list:
        new_list.append(i)
print("Original List:", lst)
print("List after removing duplicates:", new_list)
