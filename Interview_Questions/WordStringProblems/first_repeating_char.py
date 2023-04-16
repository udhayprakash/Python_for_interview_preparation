"""
Problem:
You are given a string S, in which one letter occurs twice. Every other letter occurs at most once.
Write a function:
def solution (S)
which, given a string S, returns a single-character string: the letter that occurs twice.
Examples:
1. Given S = "aba", the function should return "a".
2. Given S = "zz", the function should return "z".
3. Given S = "codility", the function should return "i". Assume that:
⚫ the length of string S is within the range [2..27]; ⚫ string S is made only of lowercase letters (a-z);
⚫ all letters in S are distinct except one, which occurs twice.
"""


def solution(S):
    processed = {}
    for char in S:
        if char in processed:
            return char
        processed[char] = 1


assert solution("aba") == "a"
assert solution("zz") == "z"
assert solution("codility") == "i"
assert solution("abcdefg") == None
