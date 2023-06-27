#!/usr/bin/python3
"""
Problem: Longest substr Without Repeating Characters

For example:
    Input: s = "abcadbb"
    Output: 3 Explanation: The answer is "abc", with the length of 3.

    Input: s = "bbbbb"
    Output: 1 Explanation: The answer is "b", with the length of 1.

    Input: s = "pwwkew"
    Output: 3 Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

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
            largestSubStrLen = max(largestSubStrLen, len(substr))
            substr = ""
        substr += each_chr

    if substr:
        largestSubStrLen = max(largestSubStrLen, len(substr))
    return largestSubStrLen


def longest_substring(somestring: str) -> int:
    largestSubStrLen = 0
    substr_chars = {}
    for ch in somestring:  # O(n)
        if ch in substr_chars:
            substr = "".join(substr_chars.keys())
            largestSubStrLen = max(len(substr), largestSubStrLen)
            substr_chars.clear()
        substr_chars[ch] = 1

    if substr_chars:
        substr = "".join(substr_chars.keys())
        largestSubStrLen = max(len(substr), largestSubStrLen)

    return largestSubStrLen


if __name__ == "__main__":
    assert longest_substring("abcadbb") == 3  # "abc"
    assert longest_substring("abcacdbb") == 4  # "acdb"
    assert longest_substring("bbbbb") == 1  # "b"
    assert longest_substring("pwwkew") == 3  # "wke"

    assert longest_substring("abcadef") == 4  # 'bcadef'
    assert longest_substring("abccba") == 3  # 'abc'
    assert longest_substring("abcd") == 4  # 'abcd'
    assert longest_substring("abcdefgha") == 8  # 'abcdefgh'

    print(
        longest_substring(
            "amjMVRoQJWcusNZDMjgjUDOGNzwamdQpLOYTBgbwhiEIUPfjAmZJUNwChrWAcEBKYKtNNAFnXiZeUgAtRDveRAFaNSASYCaJbxFQZUgeLNcPQFoYwCYGDSoPrhZKXkpsREfHSuCbHKHnofNBNMHzMqLMwbneOcJbcSgnfgbVUSQbUveAUMTdoghwULyfkWEOOFWKFikcHAZDIiKdTrOXEYwCTdPODAcuYefLFdwrmJkSiztDQGKPKlgnP"
        )
    )
