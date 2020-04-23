#!/usr/bin/python
"""
Purpose: Splitting a string without using str.split()
"""


def split_string(word):
    result = []
    temp_val = ''
    for each_char in word:
        if each_char == ':':
            result.append(temp_val)
            temp_val = ''
        else:
            temp_val += each_char
    else:
        result.append(temp_val)
    return result


if __name__ == '__main__':
    assert split_string('a:b:c:324324:45') == ['a', 'b', 'c', '324324', '45']
    assert split_string('a:b:c::324324:45') == ['a', 'b', 'c', '', '324324', '45']
