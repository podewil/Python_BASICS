nums = [0, 1, 2, 3, 4]
print(nums)         # Prints "[0, 1, 2, 3, 4]"
print(nums[2:4])    # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print(nums[2:])     # Get a slice from index 2 to 4 (exclusive); prints "[2, 3, 4]"
print(nums[:2])     # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
print(nums[:])      # Get a slice of the whole list; prints  "[0, 1, 2, 3, 4]"
print(nums[:-1])    # Slice indices can be negative; prints  "[0, 1, 2, 3]"
nums[2:4] = [8, 9]  # Assign a new sublist to a slice
print(nums)
print()


num1 = list(range(5))
print(num1)         # Prints "[0, 1, 2, 3, 4]"
print(num1[2:4])    # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print(num1[2:])     # Get a slice from index 2 to 4 (exclusive); prints "[2, 3, 4]"
print(num1[:2])     # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
print(num1[:])      # Get a slice of the whole list; prints  "[0, 1, 2, 3, 4]"
print(num1[:-1])    # Slice indices can be negative; prints  "[0, 1, 2, 3]"
num1[2:4] = [8, 9]  # Assign a new sublist to a slice
print(num1)

import numpy as np
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(b[:,1])       # Prints out arrary [2 6 10]

print(b[-1, :])     # Prints out array [9, 10, 11, 12]

print(b[-1, ...])   # Prints out array [9, 10, 11, 12]

print(b[0:2, :])    # Prints out array [[1 2 3 4]
                    #                    [5 6 7 8]]

print(b[:, 1:2])    # Prints out array [[2]
                    #                   [6]
                    #                   [10]]

print(b[:, 3:3])    # Note!! this will print out "[]"

print(b[:, 3:7])    # Note!! even if the index is out of bounds
                    # this will print out "[[4]
                    #                       [8]
                    #                       [12]]"

print(b[:, [-1]])   # Note!! this will print out "[[4]
                    #                       [8]
                    #                       [12]]"


print(b[:, -1])     # Note!! this will print out [ 4  8 12]