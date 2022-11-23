#!/usr/bin/python
"""
Purpose: https://leetcode.com/problems/first-missing-positive/submissions/

    Given an unsorted integer array, find the smallest missing positive integer.

NOTE: Your algorithm should run in O(n) time and uses constant extra space.
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted({i for i in nums if i > 0})
        if (not nums) or nums[0] != 1:
            return 1
        for _index, num in enumerate(nums):
            if _index and num - nums[_index - 1] > 1:
                return nums[_index - 1] + 1
        return nums[-1] + 1


if __name__ == "__main__":
    assert Solution().firstMissingPositive([1, 2, 0]) == 3
    assert Solution().firstMissingPositive([3, 4, -1, 1]) == 2
    assert Solution().firstMissingPositive([7, 8, 9, 11, 12]) == 1
