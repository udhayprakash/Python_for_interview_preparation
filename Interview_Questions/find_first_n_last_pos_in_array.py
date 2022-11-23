"""
Problem:
    Given an array of integers nums sorted in increasing order,
    find the starting and ending position of a given target value.

    values    - 1 2 3 3 4 5 6
    positions - 0 1 2 3 4
    Target = 3
    expected Result - 2, 4

"""


def find_leftmost_pos(arr, target_num):
    lowIndex = midIndex = 0
    highIndex = len(arr) - 1
    if arr[lowIndex] == target_num:
        return lowIndex
    while lowIndex <= highIndex:
        midIndex = (lowIndex + highIndex) // 2
        if arr[midIndex] < target_num:
            lowIndex = midIndex + 1

        elif (arr[midIndex] > target_num) or (arr[midIndex - 1] == target_num):
            highIndex = midIndex - 1
        else:
            return midIndex

    return -1


def find_rightmost_pos(arr, target_num):
    lowIndex = midIndex = 0
    highIndex = len(arr) - 1
    if arr[highIndex] == target_num:
        return highIndex

    while lowIndex <= highIndex:
        midIndex = (lowIndex + highIndex) // 2

        if (arr[midIndex] < target_num) or (arr[midIndex + 1] == target_num):
            lowIndex = midIndex + 1

        elif arr[midIndex] > target_num:
            highIndex = midIndex - 1
        else:
            return midIndex

    return -1


def get_first_n_last_pos(arr, target_num):
    first_pos = find_leftmost_pos(arr, target_num)
    last_pos = find_rightmost_pos(arr, target_num)

    return (first_pos, last_pos)


if __name__ == "__main__":
    assert get_first_n_last_pos([1, 2, 3, 4, 5, 6], 3) == (2, 2)
    assert get_first_n_last_pos([3, 3, 3, 3, 3, 3], 3) == (0, 5)
    assert get_first_n_last_pos([1, 3, 3, 3, 3, 4], 3) == (1, 4)
    assert get_first_n_last_pos([1, 2, 3, 3, 4, 5], 3) == (2, 3)
    assert get_first_n_last_pos([1, 2, 3, 4, 5, 6], 3) == (2, 2)
    assert get_first_n_last_pos([1, 2, 4, 5, 6, 7], 3) == (-1, -1)
