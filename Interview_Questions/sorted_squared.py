"""
Purpose: Given an array of integers sorted in ascending order as input,
    return the output array as squares of them, in non-decreasing

"""


def return_sorted_squares(nums):  # O(nlogn)
    return sorted([num**2 for num in nums])


def return_sorted_squares(nums):  # O(n)
    sqr_nums = []
    left_flag, right_flag = 0, len(nums) - 1
    while left_flag <= right_flag:
        left_sqr = pow(nums[left_flag], 2)
        right_sqr = pow(nums[right_flag], 2)
        if left_sqr <= right_sqr:
            sqr_nums.insert(0, right_sqr)
            right_flag -= 1
        else:
            sqr_nums.insert(0, left_sqr)
            left_flag += 1
    return sqr_nums


assert return_sorted_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
