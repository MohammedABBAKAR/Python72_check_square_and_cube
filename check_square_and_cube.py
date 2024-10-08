

# Squares and Cubes
# Create a function that takes a list of two numbers and checks if the square root of the first number is equal to the cube root of the second number.

# Examples
# check_square_and_cube([4, 8]) ➞ True

# check_square_and_cube([16, 48]) ➞ False

# check_square_and_cube([9, 27]) ➞ True
# Notes
# Remember to return either True or False.
# All lists contain two positive numbers.


import math

def check_square_and_cube(lst):
    # Check if the square root of the first number equals the cube root of the second number
    return math.isclose(math.sqrt(lst[0]), math.pow(lst[1], 1/3))

# Test cases
test_cases = [
    [4, 8],    # True
    [16, 48],  # False
    [9, 27]    # True
]

results = {str(test): check_square_and_cube(test) for test in test_cases}
results
print(check_square_and_cube([4, 8]))
print(results)