"""
Purpose: Given an unsorted array of integers, find the length of the
    longest consecutive elements sequence.

    Input : [100, 4, 200, 1, 2, 3]
    Output: 4
"""


def longest_consecutive_sequence_length(nums):
    nums = sorted(set(nums))

    count, max_len = 0, 0
    for index, num in enumerate(nums):
        if index == 0:
            count += 1
            continue
        if num - nums[index - 1] == 1:
            count += 1
            continue

        if count > max_len:
            max_len = count
        count = 1
    return max_len


assert longest_consecutive_sequence_length([100, 4, 200, 1, 2, 3]) == 4
assert longest_consecutive_sequence_length([100, 4, 101, 1, 2, 3]) == 4
assert longest_consecutive_sequence_length([100, 4, 1, 1, 2, 3]) == 4
