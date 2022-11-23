class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp = [0 for _ in range(len(nums))]
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)


ob1 = Solution()

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
assert ob1.maxSubArray(nums) == 6
print(ob1.maxSubArray(nums))
