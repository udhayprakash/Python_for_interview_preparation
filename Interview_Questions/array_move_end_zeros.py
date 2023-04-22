"""
Purpose: Given an array can you move the zeros to the end while
    maintaining the relative order of the other elements

"""


def move_end(arr, number=0):
    zeros_indices = [i for i, val in enumerate(arr) if val == number]
    for i in zeros_indices[::-1]:
        del arr[i]
    return arr + [0] * len(zeros_indices)


if __name__ == "__main__":
    print(move_end([1, 0, 3, 12, 4, 0, 2]))
    assert move_end([1, 0, 3, 12, 4, 0, 2]) == [1, 3, 12, 4, 2, 0, 0]
    assert move_end([1, 0, 3, 12, 4, 0, 2, 0]) == [1, 3, 12, 4, 2, 0, 0, 0]
    assert move_end([1, 0, 3, 12, 4, 0, 0]) == [1, 3, 12, 4, 0, 0, 0]
