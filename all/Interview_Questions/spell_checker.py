#!/usr/bin/python
"""
Purpose: Write a (bad) spell checker

The product department needs a quick and dirty spell-checker.

Should return a correctly spelled word if found, otherwise return None.

1. A correctly spelled word is defined as one that appears in the list
2. A matching input word would have
    a. The same combination of characters are the valid word
    b. The same number of total characters as the valid word
    OR
    c. Beginning of partial word i.e., like '%word' search in SQL

"""

valid_words = ("cat", "bat")


def spell_checker(word):
    for each_word in valid_words:
        if (
            each_word == word
            or each_word.startswith(word)
            or sorted(each_word) == sorted(word)
        ):
            return each_word


if __name__ == "__main__":
    assert spell_checker("cat") == "cat"
    assert spell_checker("act") == "cat"
    assert spell_checker("tac") == "cat"
    assert spell_checker("atc") == "cat"
    assert spell_checker("ca") == "cat"
    assert spell_checker("ba") == "bat"
    assert spell_checker("acct") == None
    assert spell_checker("batty") == None
    assert spell_checker("bats") == None
    assert spell_checker("at") == None
