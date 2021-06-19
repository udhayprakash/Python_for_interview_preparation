#!/usr/bin/python3
"""
Purpose: https://codingbat.com/prob/p118406
"""


def make_bricks(small, big, goal):
    smallVal = 1
    bigVal = 5
    if (small * smallVal + big * bigVal) == goal:
        return True
    if big == 0:
        return goal <= (small * smallVal)
    if small == 0:
        return (goal // bigVal) <= big

    
    if 0 <= (goal - (big * bigVal)) <= small:
        return True
    elif (goal - (small * smallVal)) // bigVal == 0:
        return True
    bigs = goal//bigVal
    if bigs <= big and (goal - bigs* bigVal) <=small:
        return True
    return False


assert make_bricks(3, 2, 8) == True  # 3 * small + 1 * big
assert make_bricks(1, 4, 11) is True  # 1 * 1 + 2 * 5

assert make_bricks(0, 0, 0) is True
assert make_bricks(0, 0, 1) is False

assert make_bricks(20, 0, 19) is True
assert make_bricks(6, 0, 11) is False

assert make_bricks(0, 3, 10) is True  # (10 //5) <= 3
assert make_bricks(0, 2, 10) is True

assert make_bricks(3, 1, 7) is True    # 2 * 1 + 1 * 5
assert make_bricks(7, 1, 11) is True   # 6 * 1 + 1 * 5
assert make_bricks(7, 1, 8) is True    # 3 * 1 + 1 * 5
assert make_bricks(43, 1, 46) is True  #
assert make_bricks(40, 2, 47) is True
assert make_bricks(20, 4, 39) is True

assert make_bricks(3, 1, 8) == True
assert make_bricks(3, 2, 10) == True
assert make_bricks(3, 1, 9) == False # 3 *1
assert make_bricks(3, 1, 8) is True
assert make_bricks(3, 1, 9) is False
assert make_bricks(3, 2, 10) is True
assert make_bricks(3, 2, 8) is True

assert make_bricks(3, 2, 9) is False
assert make_bricks(6, 1, 11) is True
assert make_bricks(1, 4, 12) is False
assert make_bricks(1, 1, 7) is False
assert make_bricks(2, 1, 7) is True
assert make_bricks(40, 1, 46) is False
assert make_bricks(40, 2, 50) is True
assert make_bricks(40, 2, 52) is False
assert make_bricks(22, 2, 33) is False
assert make_bricks(1000000, 1000, 1000100) is True
assert make_bricks(2, 1000000, 100003) is False
assert make_bricks(20, 0, 21) is False
assert make_bricks(20, 4, 51) is False


assert make_bricks(7, 1, 13) is False
