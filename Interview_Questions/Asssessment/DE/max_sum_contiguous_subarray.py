"""
Problem:
    Write a Python function that takes in a list of integers
    (in this case use 1, -2, 3, 4, -5 and 6) and
    returns the maximum sum of any contiguous subarray of the list.
    A subarray is a contiguous portion of the list.

"""


def max_sum_contiguous_subarray(numbers):
    if not numbers:
        return 0

    current_sum, max_sum = 0, numbers[0]

    for num in numbers:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        # Reset current_sum to 0 if it becomes negative
        current_sum = max(0, current_sum)
    return max_sum


# Assert statements to test max_sum_contiguous_subarray() function

# Case 1: List with positive numbers
assert max_sum_contiguous_subarray([1, 2, 3, 4, 5]) == 15
assert max_sum_contiguous_subarray([11, 2, 3, 4, 5]) == 25
assert max_sum_contiguous_subarray([2, 4, 6, 8, 10]) == 30

# Case 2: List with negative numbers
assert max_sum_contiguous_subarray([-1, -2, -3, -4, -5]) == -1
assert max_sum_contiguous_subarray([-2, -4, -6, -8, -10]) == -2
assert max_sum_contiguous_subarray([-5, -1, -3, -7, -9]) == -1

# Case 3: List with mix of positive and negative numbers
assert max_sum_contiguous_subarray([1, -2, 3, 4, -5, 6]) == 8
assert max_sum_contiguous_subarray([11, -2, 3, 4, -5, 6]) == 17
assert max_sum_contiguous_subarray([2, -3, 5, 8, -4, 2]) == 13

# Case 4: List with all negative numbers
assert max_sum_contiguous_subarray([-1, -2, -3, -4, -5, -6]) == -1
assert max_sum_contiguous_subarray([-10, -2, -3, -4, -5, -6, -7]) == -2

# Case 5: Empty list
assert max_sum_contiguous_subarray([]) == 0

# Case 6: List with only one element
assert max_sum_contiguous_subarray([5]) == 5
assert max_sum_contiguous_subarray([-7]) == -7
