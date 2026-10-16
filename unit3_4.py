#Practical4: Write a program that takes a list of integers and returns a list of all possible permutations of the input list.
Input: [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
from itertools import permutations
numbers = [1, 2, 3]
for p in permutations(numbers):
  	print(list(p))
