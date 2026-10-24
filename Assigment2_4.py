#4. Write a Python program to accept a string and another string from the user. Perform the following operations:
# a) Display the strings and their lengths using len().
# b) Access characters using positive and negative indexing.
# c) Extract substrings using slicing.
# d) Repeat a string using * and concatenate two strings using +.
# e) Check whether a character or substring exists using in and not in.
# f) Compare two strings using ==, !=, <, and >.
# g) Convert strings into uppercase and lowercase using upper() and lower().

#4. Write a Python program to accept two strings from the user.

# Accept two strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# a) Display strings and their lengths
print("First String:", str1)
print("Second String:", str2)
print("Length of First String:", len(str1))
print("Length of Second String:", len(str2))

# b) Access characters using positive and negative indexing
print("Positive Indexing:", str1[0])
print("Negative Indexing:", str1[-1])

# c) Extract substrings using slicing
print("Slicing of First String:", str1[0:3])
print("Slicing of Second String:", str2[0:3])

# d) Repeat and concatenate strings
print("String Repetition:", str1 * 2)
print("String Concatenation:", str1 + str2)

# e) Check whether a character or substring exists
ch = input("Enter character or substring to search: ")
print("Using in:", ch in str1)
print("Using not in:", ch not in str1)

# f) Compare two strings
print("Equal (==):", str1 == str2)
print("Not Equal (!=):", str1 != str2)
print("Less Than (<):", str1 < str2)
print("Greater Than (>):", str1 > str2)

# g) Convert strings into uppercase and lowercase
print("First String in Uppercase:", str1.upper())
print("First String in Lowercase:", str1.lower())
print("Second String in Uppercase:", str2.upper())
print("Second String in Lowercase:", str2.lower())