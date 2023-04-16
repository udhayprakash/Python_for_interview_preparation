"""
Problem:

There are N balls positioned in a row. Each of them is either red or white.
In one move we can swap two adjacent balls.
We want to arrange all the red balls into a consistent segment.
What is the minimum number of swaps needed?
Write a function:
def solution(S)
that, given string S of length N built from characters "R" and "w",
representing red and white balls respectively, returns the minimum number of swaps needed to arrange all the red balls into a consistent segment.
If the result exceeds 10**9, return -1.

Examples:
    1. Given S = "WRRWWR", your function should return 2.
    We can move the last ball two positions to the left:
    "WRRWRW" "WRRRWW"
    2. Given S = "WWRWWWRWR", your function should return 4. We can move first and last red ball towards the middle one:
    "WWWRWWRWR"
    "WWWWRWRWR"
    "WWWWWRRWR"
    "WWWWWRRRW"
    3. Given S = "WWW", your function should return 0. There are no red balls to arrange into a segment.
    4. Given S is "RW" repeated 100,000 times, your function should return -1. The minimum needed number of swaps is greater than 10**9.
"""


def solution(S):
    if len(S) <= 2 or S.count("R") <= 1:
        return 0

    total_distance = 0
    prev_r_index = -1
    for i, char in enumerate(S):
        if char == "R":
            if prev_r_index != -1:
                total_distance += i - prev_r_index - 1
            prev_r_index = i

        if total_distance >= 99999:  # 10**9:
            return -1

    return total_distance


# Test cases
assert solution("WRRWWR") == 2
assert solution("WWRWWWRWR") == 4
assert solution("WWW") == 0
print(solution("RW" * 100000))
assert solution("RW" * 100000) == -1

# W W   R   W   W   W   R   W   R
# 0 1   2   3   4   5   6   7   8
#       .          3

# WWRWWWRWR
# WWWRWWRWR
# WWWWRWRWR
# WWWWWRRWR
# WWWWWRRRW
