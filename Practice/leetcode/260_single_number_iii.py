#!/usr/bin/python
"""
Purpose: https://leetcode.com/problems/single-number-iii/

    Given an array of numbers nums, in which exactly two elements
    appear only once and all the other elements appear exactly twice.
    Find the two elements that appear only once.

Note:
    The order of the result is not important.
    Your algorithm should run in linear runtime complexity.
    Could you implement it using only constant space complexity?
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if nums.count(num) == 1:
                result.append(num)
        return result

    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        xor = xor & (xor - 1) ^ xor
        a = b = 0
        for num in nums:
            if xor & num:
                a ^= num
            else:
                b ^= num
        return [a, b]


if __name__ == "__main__":
    assert Solution().singleNumber([1, 2, 1, 3, 2, 5]) == [3, 5]
