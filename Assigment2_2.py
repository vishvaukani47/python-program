#2. Write a Python program to create a list containing the names of five students (list1)and a nested list containing the names and marks of at least five students(list2). Perform the following operations:
# a) Accept a student name from the user and search for it in the student list. Display its index if found; otherwise, display an appropriate message.
# b) Sort student names in ascending and descending alphabetical order using sort() and sorted().
# c) Add a new student name, insert a name at a specified position, and remove a student name.
# d) Display all student records using a loop(list2).
# e) Find the student who obtained the highest marks and calculate the average marks(list2).
# f)  Display the number of student records using len()(list2).

#2. Write a Python program to create a list containing names of five students (list1)
# and a nested list containing names and marks of five students (list2).

# Create list1
list1 = ["Amit", "Riya", "Rahul", "Priya", "Neha"]

# Create nested list2
list2 = [["Amit", 85], ["Riya", 90], ["Rahul", 75],
         ["Priya", 95], ["Neha", 80]]

# a) Search for a student name
name = input("Enter student name to search: ")

if name in list1:
    print("Student found at index:", list1.index(name))
else:
    print("Student not found")

# b) Sort student names in ascending and descending order
print("Ascending Order:", sorted(list1))

list1.sort(reverse=True)
print("Descending Order:", list1)

# c) Add, insert, and remove student names
list1.append("Karan")
print("After adding student:", list1)

list1.insert(2, "Jay")
print("After inserting student:", list1)

list1.remove("Jay")
print("After removing student:", list1)

# d) Display all student records
print("Student Records:")
for student in list2:
    print("Name:", student[0], "Marks:", student[1])

# e) Find student with highest marks and calculate average marks
highest = max(list2, key=lambda x: x[1])
print("Highest Marks:", highest[0], highest[1])

total = 0
for student in list2:
    total = total + student[1]

average = total / len(list2)
print("Average Marks:", average)

# f) Display number of student records
print("Number of Student Records:", len(list2))