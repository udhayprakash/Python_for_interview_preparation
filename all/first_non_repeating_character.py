#!/usr/bin/python
"""
Purpose: To get the first non-repeating character in the given string
"""
__name__ = 'Author'


def get_first_non_repeating_character(word: str):
    for each_char in word:
        if word.count(each_char) == 1:
            return each_char
    return ''


if __name__ == '__main__':
    assert get_first_non_repeating_character('TimesforTimes') == 'f'
    assert get_first_non_repeating_character('TimesQuiz') == 'T'
    assert get_first_non_repeating_character('aaa') == ''
