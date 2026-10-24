#1. Write a Python program to create a list of ten integers using the range() function. Perform the following operations:
# a) Display the list and access its elements using positive indexing, negative indexing, and slicing.
# b) Update an element at a specified index entered by the user.
# c) Perform list concatenation using + and repetition using *.
# d) Check whether a number exists in the list using in and not in.
# e) Perform the following list methods: append(), insert(), remove(), pop(), reverse(), and count().
# f) Display the list in ascending and descending order using sort() and sorted().
# g) Create an alias and a clone of the list, modify one element, and demonstrate the difference between aliasing and cloning.
# h) Display the maximum, minimum, and length of the list using max(), min(), and len().


#1. Write a Python program to create a list of ten integers using range() function.

# Create a list of ten integers using range()
mylist = list(range(1, 11))

# a) Display list and access elements using indexing and slicing
print("Original List:", mylist)
print("Positive Indexing:", mylist[2])
print("Negative Indexing:", mylist[-1])
print("Slicing:", mylist[2:7])

# b) Update an element at a specified index
index = int(input("Enter index to update: "))
value = int(input("Enter new value: "))
mylist[index] = value
print("Updated List:", mylist)

# c) List concatenation and repetition
print("Concatenation:", mylist + [11, 12, 13])
print("Repetition:", mylist * 2)

# d) Check whether a number exists in the list
num = int(input("Enter number to search: "))
print("Using in:", num in mylist)
print("Using not in:", num not in mylist)

# e) Perform list methods
mylist.append(20)
print("After append():", mylist)

mylist.insert(2, 15)
print("After insert():", mylist)

mylist.remove(15)
print("After remove():", mylist)

mylist.pop()
print("After pop():", mylist)

mylist.reverse()
print("After reverse():", mylist)

print("Count of 5:", mylist.count(5))

# f) Sort list in ascending and descending order
print("Ascending Order:", sorted(mylist))

mylist.sort()
print("Sorted List:", mylist)

mylist.sort(reverse=True)
print("Descending Order:", mylist)

# g) Create alias and clone of the list
alias = mylist
clone = mylist.copy()

mylist[0] = 100

print("Original List:", mylist)
print("Alias List:", alias)
print("Clone List:", clone)

# h) Display maximum, minimum, and length
print("Maximum:", max(mylist))
print("Minimum:", min(mylist))
print("Length:", len(mylist))