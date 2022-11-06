#!/usr/bin/python
"""
Purpose: Program to validate whether an entered word is palindrome
"""
from time import perf_counter_ns


def palindrome_validation_pythonic(test_word):
    return test_word == test_word[::-1]


start_time = perf_counter_ns()
assert palindrome_validation_pythonic("otto") is True
print("Method 1 duration(ns):", perf_counter_ns() - start_time)


def palindrome_validation_without_slicing(test_word):
    """Implementing without string slicing"""
    str_len = len(test_word)
    for index, ch in enumerate(test_word):
        if ch != test_word[str_len - index - 1]:
            return False
    return True


start_time = perf_counter_ns()
assert palindrome_validation_without_slicing("otto") is True
print("Method 2 duration(ns):", perf_counter_ns() - start_time)


def palindrome_validation_without_slicing(test_word):
    """Implementing without string slicing"""
    str_len = len(test_word)
    for i in range(str_len):
        if test_word[i] != test_word[str_len - 1 - i]:
            return False
    return True


start_time = perf_counter_ns()
assert palindrome_validation_without_slicing("otto") is True
print("Method 3 duration(ns):", perf_counter_ns() - start_time)


# Method 1 duration(ns): 4800
# Method 2 duration(ns): 5300
# Method 3 duration(ns): 4100
