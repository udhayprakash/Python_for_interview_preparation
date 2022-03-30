#!/usr/bin/python
"""
Purpose: Find the longest substring 
    with each substring containing two unique characters,
    in ascending order
"""


def get_longest_substr(sentence):
    repeat_chars = []
    temp = sentence[0]
    for each_char in sentence[1:]:
        if temp[-1] == each_char:
            temp += each_char
        else:
            repeat_chars.append(temp)
            temp = each_char
    longest_substr = ''
    for index, each_repeat_chars in enumerate(repeat_chars):
        if index:
            substr = repeat_chars[index - 1] + each_repeat_chars
            if len(substr) > len(longest_substr):
                longest_substr = ''.join(sorted(substr))
    return longest_substr


if __name__ == '__main__':
    assert get_longest_substr(
        'cbbbbbaaaaadddddddeeeeffffffffg') == 'aaaaaddddddd'
