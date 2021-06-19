#!/usr/bin/python3
def centered_average(nums):
    nums.sort()
    nums = nums[1:-1]
    return int(sum(nums)/len(nums))  # int() needed in python3


def centered_average(nums):
    min_val = nums[0]
    max_val = nums[0]
    summation = 0
    for num in nums:
        summation += num
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    summation = summation - min_val - max_val
    return int(summation/(len(nums) - 2))


assert centered_average([1, 2, 3, 4, 100]) == 3
assert centered_average([1, 1, 5, 5, 10, 8, 7]) == 5
assert centered_average([-10, -4, -2, -4, -2, 0]) == -3
