#Practical5: Rotate a List by N Positions - Write a program that rotates a list by n positions to the right.
numbers = [1, 2, 3, 4, 5]
n = 2
while n > 0:
    last = numbers.pop()
    numbers.insert(0, last)
    n = n - 1
print(numbers)
