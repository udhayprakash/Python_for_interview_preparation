#!/usr/bin/python
"""
Purpose: Implement an algorithm to determine if a string contains all
    unique characters. Assume that only characters a-z are permitted.
"""
def is_unique_characters(value):
    return True if len(value) == len(set(value)) else False

assert is_unique_characters('abc')
assert is_unique_characters('aaa') == False
assert is_unique_characters('abbc') == False
assert is_unique_characters('abcdefghijklmnopqrstuvwxyz')
assert is_unique_characters('abcdefghijklmnopqrstuvwxyzz') == False
