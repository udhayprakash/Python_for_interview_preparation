#!/usr/bin/python3
"""
Question
--------
Given two strings "a" and "z", return TRUE if "a" is subsequence of "z", or FALSE otherwise.

Subsequence Definition:
	String "a" is subsequence of String "z" if the characters in String "a" appear in the
    same order (contiguous or otherwise) in String "z".

NOTE: An empty string is a subsequence of every string.
"""


def issubstring(substr, word):
    if substr == "":  # empty string is substr of any string
        return True
    prevIndex, currIndex = 0, 0
    for substrIndex, substrChar in enumerate(substr):
        currIndex = word.find(substrChar)
        if word.count(substrChar) > 1:
            currIndex = word.find(substrChar, prevIndex)
        print(substrChar, prevIndex, currIndex, word.count(substrChar))
        # position of each character in substring, should be in sequence
        if currIndex == -1 or (substrIndex != 0 and prevIndex > currIndex):
            return False
        prevIndex = currIndex
    return True


# assert issubstring("", "abcde") is True
# assert issubstring("ace", "abcde") is True
# assert issubstring("aec", "abcde") is False
# assert issubstring("acp", "abcde") is False
# assert issubstring("ape", "apple") is True
# assert issubstring("apa", "apple") is False
assert issubstring("app", "apple") is False
