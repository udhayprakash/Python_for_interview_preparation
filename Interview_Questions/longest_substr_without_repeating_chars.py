#!/usr/bin/python3
"""
Problem: Longest substr Without Repeating Characters

For example:
"abccba" -> 3 since "abc" or "cba" are substrs without repeating characters
"abcd" -> 4 since no characters repeat
"abcdefgha" -> 8 since only the last character repeats
"abcadef" -> ?
"""


def longest_substring(somestring: str) -> int:
    largestSubStrLen = 0
    substr = ""
    for each_chr in somestring:  # O(n^2)
        if each_chr in substr:
            substr_len = len(substr)
            if largestSubStrLen < substr_len:
                largestSubStrLen = substr_len
            substr = ""
        substr += each_chr
    if substr:
        substr_len = len(substr)
        if largestSubStrLen < substr_len:
            largestSubStrLen = substr_len
    return largestSubStrLen


assert longest_substring("abcadef") == 4  # 'bcadef'
assert longest_substring("abccba") == 3  # 'abc'
assert longest_substring("abcd") == 4  # 'abcd'
assert longest_substring("abcdefgha") == 8  # 'abcdefgh'
