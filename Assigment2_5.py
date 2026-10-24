#5. Write a Python program to accept a sentence from the user and perform the following operations: Remove leading and trailing spaces using lstrip(), rstrip(), and strip().
# a) Search for a substring using find() and index(). Handle cases where the substring is not found.
# b) Count the occurrences of a specified word using count().
# c) Replace a word or character using replace().
# d) Split the sentence into words using split() and join them using join().
# e) Demonstrate string immutability by attempting to modify a character through indexing, and explain why the operation is not permitted.
# f) . Sort the words alphabetically and display the sorted result.

#5. Write a Python program to accept a sentence from the user.

sentence = input("Enter a sentence: ")

# Remove leading and trailing spaces
print("Using lstrip():", sentence.lstrip())
print("Using rstrip():", sentence.rstrip())
print("Using strip():", sentence.strip())

# a) Search for a substring using find() and index()
sub = input("Enter substring to search: ")

print("Using find():", sentence.find(sub))

if sub in sentence:
    print("Using index():", sentence.index(sub))
else:
    print("Substring not found")

# b) Count occurrences of a word
word = input("Enter word to count: ")
print("Occurrences:", sentence.count(word))

# c) Replace a word or character
old = input("Enter word to replace: ")
new = input("Enter new word: ")
print("After replace():", sentence.replace(old, new))

# d) Split sentence into words and join them
words = sentence.split()
print("After split():", words)

joined = " ".join(words)
print("After join():", joined)

# e) Demonstrate string immutability
try:
    sentence[0] = 'A'
except TypeError:
    print("String cannot be modified using indexing")
    print("Strings are immutable in Python")

# f) Sort words alphabetically
sorted_words = sorted(words)
print("Words in alphabetical order:", sorted_words)