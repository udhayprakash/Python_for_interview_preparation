from collections import defaultdict


class Solution:
    def isCircle(self, A, N) -> str:
        A.sort(key=len)
        results = defaultdict(int)
        for wd in A:
            for i in range(len(wd)):
                results[wd] = max(results[wd], results[wd[:i] + wd[i + 1 :]] + 1)
        return "Yes" if max(results.values()) else "No"


if __name__ == "__main__":
    N = int(input())
    A = list(input().split(" "))
    solution = Solution()
    print(solution.isCircle(A, N))

if __name__ == "__main__":
    # N = int(input())
    # A = list(input().split(" "))
    solution = Solution()
    # print(solution.isCircle(A, N))
    assert solution.isCircle(["aaa"], 1) == "Yes"
    assert solution.isCircle(["aab"], 1) == "No"
    assert solution.isCircle(["aaa", "bbb"], 2) == "No"
    assert solution.isCircle(["nib", "ban"], 2) == "Yes"
    assert solution.isCircle(["aab", "bac", "aaa", "cda"], 4) == "Yes"
    assert solution.isCircle(["aaa", "bbb", "baa", "aab"], 4) == "Yes"
    assert solution.isCircle(["ijk", "kji", "abc", "cba"], 4) == "No"
