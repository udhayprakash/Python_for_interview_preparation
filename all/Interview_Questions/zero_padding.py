#!/usr/bin/python3
"""
Purpose: In the given array, add a 0 next to 0, 
    if present in the list. 
"""


def myfunc(mylist):
    zero_pos = [i for i, num in enumerate(mylist)
                if num == 0]

    length = len(mylist)
    for index, pos in enumerate(zero_pos):
        mylist.insert(pos + index, 0)
    return mylist[:length]


if __name__ == '__main__':
    assert myfunc([1, 0, 2, 3, 0, 4, 5, 0]) == [1, 0, 0, 2, 3, 0, 0, 4]
    assert myfunc([1, 0, 2, 3]) == [1, 0, 0, 2]
