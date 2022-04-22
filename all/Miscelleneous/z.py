class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        N = len(ratings)
        candy = [1] * N
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)
        print(candy)
        return sum(candy)


print(Solution().candy([1, 2, 4, 5, 3]))
