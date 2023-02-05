#!/usr/bin/python3
"""
Problem: Given a string, find its 1st non-repeating char
"""


def first_non_rep_char(givenStr):
    if not givenStr:
        return ""
    processed_chars = {}
    for each_char in givenStr:
        processed_chars.setdefault(each_char, 0)
        processed_chars[each_char] += 1

    for char, count in processed_chars.items():
        if count == 1:
            return char
    return ""


assert first_non_rep_char("abcdefacdefghiu") == "b"
assert first_non_rep_char("acdefacdefghiu") == "g"
assert first_non_rep_char("acdefacdefhiu") == "h"
assert first_non_rep_char("acdefacdefiu") == "i"
assert first_non_rep_char("acdefacdefu") == "u"
assert first_non_rep_char("acdefacdef") == ""
assert first_non_rep_char("") == ""

assert first_non_rep_char("TimesforTimes") == "f"
assert first_non_rep_char("TimesQuiz") == "T"
assert first_non_rep_char("aaa") == ""


def first_non_rep_char_position(givenStr):
    if not givenStr:
        return (-1, "")
    processed_chars = {}
    for index, each_char in enumerate(givenStr):
        processed_chars.setdefault(each_char, [0, 0])
        processed_chars[each_char][0] += 1  # counts
        processed_chars[each_char][1] = index  # index

    non_rep_chars = []  # [(0, ‘a’), (4, ‘c), (5, ‘g’)]
    for char, count in processed_chars.items():
        if count[0] == 1:
            non_rep_chars.append((count[1], char))  # (index, char)
    if not non_rep_chars:
        return (-1, "")
    min_index, first_char = sorted(non_rep_chars, key=lambda x: x[0])[0]  # (0, ‘a’)
    return min_index, first_char  # ‘a’


assert first_non_rep_char_position("abcdefacdefghiu") == (1, "b")
assert first_non_rep_char_position("acdefacdefghiu") == (10, "g")
assert first_non_rep_char_position("acdefacdefhiu") == (10, "h")
assert first_non_rep_char_position("acdefacdefiu") == (10, "i")
assert first_non_rep_char_position("acdefacdefu") == (10, "u")
assert first_non_rep_char_position("acdefacdef") == (-1, "")
assert first_non_rep_char_position("") == (-1, "")
