#6 Write a Python program using Python's array module to create an integer array containing at least eight elements. Perform the following operations:
# a) Display the array and access elements using indexing and slicing.
# b) Insert a new element at a specified position using insert().
# c) Remove a specified element using remove() and remove the last element using pop().
# d) Search for an element and display its index if found; otherwise, display an appropriate message.
# e) Check element membership using in and not in.
# f) Display the maximum, minimum, and length of the array.
# g) Reverse the array and display the final result.

#6. Write a Python program using Python's array module.

import array

# Create an integer array containing eight elements
arr = array.array('i', [10, 20, 30, 40, 50, 60, 70, 80])

# a) Display array and access elements using indexing and slicing
print("Array:", arr)
print("Positive Indexing:", arr[2])
print("Negative Indexing:", arr[-1])
print("Slicing:", arr[2:6])

# b) Insert a new element at a specified position
pos = int(input("Enter position to insert: "))
value = int(input("Enter value to insert: "))
arr.insert(pos, value)
print("After insert():", arr)

# c) Remove a specified element and the last element
remove_value = int(input("Enter element to remove: "))

if remove_value in arr:
    arr.remove(remove_value)
    print("After remove():", arr)
else:
    print("Element not found")

arr.pop()
print("After pop():", arr)

# d) Search for an element and display its index
search = int(input("Enter element to search: "))

if search in arr:
    print("Element found at index:", arr.index(search))
else:
    print("Element not found in array")

# e) Check element membership
num = int(input("Enter number to check membership: "))
print("Using in:", num in arr)
print("Using not in:", num not in arr)

# f) Display maximum, minimum, and length
print("Maximum:", max(arr))
print("Minimum:", min(arr))
print("Length:", len(arr))

# g) Reverse the array
arr.reverse()
print("Reversed Array:", arr)