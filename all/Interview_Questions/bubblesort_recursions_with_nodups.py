# bubble sort with no duplicates


def bubble_sort_recursion(_list: list) -> list:
    minval = float("inf")
    for num in _list:
        if num < minval:
            minval = num

    if len(_list) == 1:
        return _list

    _list = list(set(_list))
    del _list[_list.index(minval)]

    return [
        minval,
    ] + bubble_sort_recursion(_list)


unsorted = [3, 8, 9, 10, 4, 7, 6, 5, 2, 9, 3, 1]
assert bubble_sort_recursion(unsorted[:]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
