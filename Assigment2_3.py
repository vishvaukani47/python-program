#3Write a Python program to create a tuple containing at least ten values, including repeated numeric values. Perform the following operations:
# a) Display the tuple and access its elements using positive indexing, negative indexing, and slicing.
# b) Perform tuple concatenation using + and repetition using *.
# c) Check whether a specified element exists using in and not in.
# d) Find the maximum, minimum, and length using max(), min(), and len().
# e) Accept a value from the user and count its occurrences using count().
# f) Search for a specified element using index(), displaying an appropriate message if it is not found.

#3. Write a Python program to create a tuple containing at least ten values.

# Create a tuple with repeated numeric values
t = (10, 20, 30, 40, 20, 50, 60, 10, 70, 80)

# a) Display tuple and access elements using indexing and slicing
print("Tuple:", t)
print("Positive Indexing:", t[2])
print("Negative Indexing:", t[-1])
print("Slicing:", t[2:7])

# b) Tuple concatenation and repetition
print("Concatenation:", t + (90, 100))
print("Repetition:", t * 2)

# c) Check whether an element exists
num = int(input("Enter number to check: "))
print("Using in:", num in t)
print("Using not in:", num not in t)

# d) Find maximum, minimum, and length
print("Maximum:", max(t))
print("Minimum:", min(t))
print("Length:", len(t))

# e) Count occurrences of a value
value = int(input("Enter value to count: "))
print("Occurrences:", t.count(value))

# f) Search for an element using index()
search = int(input("Enter value to search: "))

if search in t:
    print("Element found at index:", t.index(search))
else:
    print("Element not found in tuple")