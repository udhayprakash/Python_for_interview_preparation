#!/usr/bin/python
"""
Purpose: Sum of Integers in a string
"""


def get_sum_of_integers(word: str):
    import re

    return sum(map(int, re.findall(r"\d", word)))


def get_sum_of_integers_1(word: str):
    result = 0
    for each_char in word:
        if each_char in "0123456789":
            result += int(each_char)
    return result


def get_sum_of_integers_2(word: str):
    import re

    return sum(map(int, re.findall(r"\d+", word)))


def get_sum_of_integers_3(word: str):
    result = 0
    previous_char = ""
    for each_char in word:
        if each_char in "0123456789":
            previous_char += each_char
        else:
            if previous_char:
                result += int(previous_char)
                previous_char = ""
    else:
        if previous_char:
            result += int(previous_char)
    return result


if __name__ == "__main__":
    assert get_sum_of_integers("asp55jh5") == 15
    assert get_sum_of_integers_1("asp55jh5") == 15
    assert get_sum_of_integers_2("asp55jh5") == 60
    assert get_sum_of_integers_3("asp55jh5") == 60
