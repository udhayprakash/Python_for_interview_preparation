#!/usr/bin/python
"""
Purpose: https://leetcode.com/problems/missing-number/

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.


"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if (not nums) or (nums[0] != 0):
            return 0
        for _index, num in enumerate(nums):
            if _index and (num - nums[_index - 1]) > 1:
                return nums[_index - 1] + 1
        return nums[-1] + 1


if __name__ == '__main__':
    assert Solution().missingNumber([3, 0, 1]) == 2
    assert Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert Solution().missingNumber([0]) == 1
    assert Solution().missingNumber([1]) == 0
    assert Solution().missingNumber([1, 2]) == 0
    assert Solution().missingNumber([4, 5, 6, 8]) == 0
