"""
Problem: Sum of Diagonals

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix is shown below:

1   2   3
4   5   6
7   8   9

Absolute difference between the left-to-right diagonal and the right-to-left diagonal
"""


def diagonal_difference(matrix):  # O(n)
    """square matrix has same rows and columns"""
    matrix_size = len(matrix)
    left_to_right_sum = 0
    right_to_left_sum = 0
    for index, row in enumerate(matrix):
        left_to_right_sum += row[index]
        right_to_left_sum += row[matrix_size - index - 1]

    return abs(left_to_right_sum - right_to_left_sum)


assert diagonal_difference([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 0

assert diagonal_difference([[1, 2, 3], [4, 5, 6], [9, 8, 9]]) == 2
