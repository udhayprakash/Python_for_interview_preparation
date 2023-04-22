"""
Problem: Find the minimum value to be added so that an array becomes balanced

    1 3 1 2 4 3
    1+3+1 = 5
    2+4+3 = 9
    4 more

"""


def min_val_for_balance(arr):
    arr_len = len(arr)
    first_half = arr[: arr_len // 2]
    second_half = arr[arr_len // 2 :]
    return abs(sum(first_half) - sum(second_half))


if __name__ == "__main__":
    assert min_val_for_balance([1, 3, 1, 2, 4, 3]) == 4
    print(min_val_for_balance([1, 3, 1, 2, 4, 3]))
