def replace_left_highest(mylist):
    result = []
    for index, _ in enumerate(mylist):
        max_val = max(mylist[index:])
        result.append(max_val)
    return result


assert replace_left_highest([1, 2, 3, 4, 5]) == [5, 5, 5, 5, 5]
assert replace_left_highest([1, 2, 3, 4, 5, 1]) == [5, 5, 5, 5, 5, 1]
assert replace_left_highest([2, 3, 4, 1, 2]) == [4, 4, 4, 2, 2]
assert replace_left_highest([2, 3, 4, 1, 2, 1, 2, 3]) == [4, 4, 4, 3, 3, 3, 3, 3]
