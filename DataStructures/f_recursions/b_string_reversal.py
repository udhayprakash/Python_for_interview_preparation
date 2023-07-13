#!/usr/bin/python
"""
Purpose: String reversal
"""
# Method 1 : Pythonic way
word = "Python"
print(f"{word[::-1] =}")

# Method 2: Using recursions
# Python  <- take first char and place at end
# ythonP
# thonPy
# honPyt
# onPyth
# nPytho
# Python


def string_reversal(given_word):
    if not given_word:
        return ""
    print(f"{given_word =}")
    return string_reversal(given_word[1:]) + given_word[0]


result = string_reversal("Python")
print(result)


# Python  # take last char and place at start
# nPytho
# onPyth
# honPyt
# thonPy
# ....


def string_reversal_1(given_word):
    if not given_word:
        return ""
    print(f"{given_word =}")
    return given_word[-1] + string_reversal_1(given_word[:-1])


result = string_reversal_1("Python")
print(result)
