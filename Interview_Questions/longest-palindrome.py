#!/usr/bin/python3
"""
Problem Name: Find Longest Palindromic Substring

Problem Statement: Given a string s, find and return the longest
    palindromic substring in s.
    You may assume that the maximum length of s is 1000.

    * Example(s): the longest palindrome in the string "ababd" is "aba" or "bab" (either is acceptable) and we would want either returned
    * Edge Cases: what happens when the string is of length 1 or 0?
    * Inputs: asdfsda, hellollehasdf, abahellollehesdf, abacdcf */regsdgsdgdsgsggsdgdsgsdgsgsgsfasfafafaf
"""


def getSubString(s, l, r):
    while l >= 0 and r < len(s) and s[r] == s[l]:
        l -= 1
        r += 1

    return s[l + 1 : r]


def longestPalindrome(s):
    largest = ""
    for i in range(len(s)):
        for k in range(2):
            temp = getSubString(s, i, i + k)
            if len(temp) > len(largest):
                largest = temp
    return largest


print(longestPalindrome("ababd"))
print(longestPalindrome("aabbaba"))
