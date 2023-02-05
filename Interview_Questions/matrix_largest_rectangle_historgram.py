"""
Python3 program to find largest rectangle with all 1s in a binary matrix
Finds the maximum area under the histogram represented by histogram.
"""


class Solution:
    def solve(self, matrix):
        res = 0
        for i in range(len(matrix)):
            res = max(res, matrix[i][0])
        for i in range(len(matrix[0])):
            res = max(res, matrix[0][i])

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] = (
                        min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1])
                        + 1
                    )

                    res = max(res, matrix[i][j])

        return res * res


ob = Solution()
matrix = [
    [1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
]

assert ob.solve(matrix) == 16
