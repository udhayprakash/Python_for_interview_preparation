#!/usr/bin/python
"""
Purpose:

NOTE: All are lower case letters , [a-z]
     When there is no solution, return -1

Example:
    initial: 'xyz'
    goal   : 'xzyxz'

    Output : 3
        'xz' + 'y' + 'xz
"""
import itertools


def generate_possibilities(word):
    _possibilities = []
    i = len(word)
    while i > 0:
        _possibilities.extend(["".join(w) for w in itertools.combinations(word, i)])
        i -= 1
    return _possibilities


def minimumConcat(initial, goal):
    res = 0
    possibilities = generate_possibilities(initial)
    for each_pos in possibilities:
        if each_pos in goal:
            res += goal.count(each_pos)
            goal = goal.replace(each_pos, "")
    return -1 if goal else res


if __name__ == "__main__":
    assert minimumConcat("xyz", "xzyxz") == 3
    assert minimumConcat("abc", "acdbc") == -1
    assert minimumConcat("abc", "abcbc") == 2
