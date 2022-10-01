# mat1 = [
#     [1, 1, 1],
#     [1, 0, 1],
#     [1, 1, 1]
# ]

# mat2 = [
#     [1, 1],
#     [0, 1]
# ]

# def myfunc(matrix):
#     for rindex, row in enumerate(matrix):
#         for cindex, ele in enumerate(row):
#             for val in (row + [rw[cindex] for rw in matrix]):
#                 if val == 0:
#                     print(row, [rw[cindex] for rw in matrix])


# print(myfunc(mat2))


# # microsoft - project mesh


dictionary = {"it": 2, "is": 2, "valid": 4, "sentence": 8}
dictionary = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))


def myfunc(sentence):
    for dword in dictionary:
        if dword in sentence:
            pos = sentence.find(dword)
            sentence = sentence[:pos] + " " + sentence[pos:]
            del dictionary[dword]
            break
    else:
        return sentence.strip()
    return myfunc(sentence)


# print( myfunc('itisvalidsentence'))
# assert myfunc('itisvalidsentence') == 'it is valid sentence'
# assert myfunc('itisvaliditsentence') == 'it is valid it sentence'

# Python3 program to find largest rectangle
# with all 1s in a binary matrix

# Finds the maximum area under the
# histogram represented
# by histogram. See below article for details.


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
print(ob.solve(matrix))
