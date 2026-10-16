#Practical2 : Write a program to create a list of numbers in the range 1 to 10. Then delete all the odd numbers from the list and print the final list.
lst = list(range(1, 11))
print("Original List:", lst)
for i in lst[:]:
    if i % 2 != 0:
        lst.remove(i)
print("Final List:", lst)
