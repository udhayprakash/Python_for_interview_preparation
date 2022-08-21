"""
Write a Program to find the second highest number in the given list
"""


def second_highest_num(arr):
    if len(arr) < 2:
        return "Invalid input"
    elif len(arr) == 2:
        return min(arr)
    else:
        firstHigh = secondHigh = float("-inf")
        for num in arr:
            if num > firstHigh:
                secondHigh = firstHigh
                firstHigh = num
            elif num > secondHigh and num != firstHigh:
                secondHigh = num
    return secondHigh


assert second_highest_num([]) == "Invalid input"
assert second_highest_num([2]) == "Invalid input"
assert second_highest_num([2, 3]) == 2
assert second_highest_num([2, 3, 2]) == 2
assert second_highest_num([2, 3, 1]) == 2
assert second_highest_num([2, 2, 1, 2]) == 1
assert second_highest_num([2, 3, 1, 3]) == 2
assert second_highest_num([2, 3, 1, 3, 1, 1, 2]) == 2
assert second_highest_num([2, 3, 1, -3, 1, 1, 2]) == 2
assert second_highest_num([2, -3, 1, -3, 1, 1, 2]) == 1
