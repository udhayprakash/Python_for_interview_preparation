"""
Problem: Given a fixed length array arr of integers, write a function
    to duplicate each occurrence of zero, shifting the remaining elements to the right.

constraints: Do not create a copy of the array (i.e, in place)

Ex 1:
    input   : [1, 0, 2, 3, 0, 4, 5, 0]
    output  : null

Bonus: rite a unit test that covers a fe corner cases.
"""


def myfunction(arr):
    i = 0
    while i < len(arr):
        if arr[i] != 0:
            i += 1
        elif arr[i] == 0:
            arr[i:] = [0] + arr[i : len(arr) - 1]
            i += 2
    return arr


assert myfunction([]) == []
assert myfunction([1]) == [1]
assert myfunction([1, 2, 3]) == [1, 2, 3]

assert myfunction([1, 0, 2, 3]) == [1, 0, 0, 2]
assert myfunction([1, 0, 2, 3, 0]) == [1, 0, 0, 2, 3]

assert myfunction(
    [
        1,
        0,
        2,
        3,
        0,
        4,
        5,
    ]
) == [1, 0, 0, 2, 3, 0, 0]
