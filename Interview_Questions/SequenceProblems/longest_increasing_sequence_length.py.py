"""
A subsequence is created by deleting zero or more elements from a sequence while maintaining order.
A sequence is strictly increasing if every element in the sequence is greater than the previous element.

For example, [1, 2, 3] is strictly increasing while [1,2, 2] is not.
Given an array of integers, determine the length of the longest strictly increasing subsequence.

For example,
    s = [1, 2, 2, 3, 1, 6]
    Two strictly increasing subsequences are (1,2), (1, 2, 3).
    The longest increasing subsequence has a length of 4: LIS = [1,2,3,6]

Function Description
    Complete the function findLIS in the editor below.
    findLIS has the following parameter(s):
        int s[n]: an array of integers
    Returns:
        int: the length of the longest strictly increasing subsequence in the array
    Constraints:
        • 1sn < 1000
        • 1 ≤ sils 1000000
        • Input Format for Custom Testing

~ Sample Case 0
    Sample Input 0
        STDIN Function Parameters
        3
        1
        4
        3
        > s[] Size = 3
        > s[] = [ 1, 4, 3 ]
    Sample Output 0
    2
    Explanation 0
    Inputs are s=[1,4,3]. Increasing subsequences are [1,4] and [1,3].
"""


def findLIS(nums: int) -> int:
    if not nums:
        return 0

    n = len(nums)
    lis = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    return max(lis)


if __name__ == "__main__":
    assert findLIS([]) == 0
    assert findLIS([1]) == 1
    assert findLIS([1, 1]) == 1
    assert findLIS([1, 3]) == 2
    assert findLIS([1, 4]) == 2
    assert findLIS([1, 4, 4]) == 2
    assert findLIS([1, 4, 3]) == 2
    assert findLIS([1, 4, 3, 4]) == 3
    assert findLIS([1, 4, 3, 4, 5]) == 4
    assert findLIS([1, 2, 2, 3, 1, 6]) == 4
    assert findLIS([1, 2, 2, 3, 1, 6, -7]) == 4
