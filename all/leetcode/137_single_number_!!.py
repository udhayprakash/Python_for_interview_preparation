#!/usr/bin/python
"""
Purpose: https://leetcode.com/problems/single-number-ii/
    Given a non-empty array of integers, every element appears three
    times except for one, which appears exactly once. Find that single one.

NOTE: Your algorithm should have a linear runtime complexity.
    Could you implement it without using extra memory?
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) == 1:
                return num

    def singleNumber(self, nums: List[int]) -> int:
        x1, x0 = 0, 0
        for num in nums:
            x1, x0 = x1 ^ (x0 & num), x0 ^ num
            mask = ~ (x1 & x0)
            x1, x0 = x1 & mask, x0 & mask
        return x0


if __name__ == '__main__':
    assert Solution().singleNumber([2, 2, 3, 2]) == 3
    assert Solution().singleNumber([0, 1, 0, 1, 0, 1, 99]) == 99
