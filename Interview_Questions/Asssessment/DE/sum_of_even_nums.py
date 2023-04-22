"""
Problem:
    Write a Python function that takes in a list of integers (0 through 10)
    and returns the sum of all the even numbers in the list
"""


def sum_of_even_numbers(numbers):
    return sum([num for num in numbers if num % 2 == 0])


# Case 1 - continuous numbers
assert sum_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30

# case 2 - all odd numbers
assert sum_of_even_numbers([1, 3, 5, 7, 9]) == 0

# case 3 - all even numbers
assert sum_of_even_numbers([2, 4, 6, 8, 10, 12]) == 42

# case 4 - empty numbers list
assert sum_of_even_numbers([]) == 0

# case 5 - all same even number
assert sum_of_even_numbers([2, 2, 2, 2, 2, 2]) == 12

# case 6 - all same odd number
assert sum_of_even_numbers([3, 3, 3, 3, 3, 3]) == 0
