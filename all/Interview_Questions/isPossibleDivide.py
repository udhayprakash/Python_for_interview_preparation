from collections import Counter


class Solution:
    def isPossibleDivide(self, A, k) -> bool:
        count = Counter(A)
        for num in sorted(count.keys()):
            c = count[num]
            if not c:
                continue
            for i in range(num, num + k):
                if count[i] < c:
                    return False
                count[i] -= c
        return True


if __name__ == "__main__":
    # A = list(map(int, input().split()))
    # k = int(input())
    solution = Solution()
    # print(solution.isPossibleDivide(A, k))
    # False when no. of digits is not multiple of given no. (3, here)
    assert solution.isPossibleDivide([1, 2, 3, 4], 3) is False
    assert solution.isPossibleDivide([1, 2, 3, 3, 4, 4, 5, 6], 4) is True
    assert solution.isPossibleDivide([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3) is True
