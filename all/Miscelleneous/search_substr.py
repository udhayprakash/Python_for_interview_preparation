#!/usr/bin/python3
"""
Purpose: 
"""


def myfunc(searchStr, paragraph):
    i = 0
    while i < len(paragraph):
        for index, char in enumerate(searchStr):
            if char != paragraph[i + index]:
                break
        else:
            return i
        i += 1
    return -1


if __name__ == '__main__':
    sentence = 'python is a cool language'

    assert myfunc('ool', sentence) == sentence.find('ool')
    assert myfunc('java', sentence) == sentence.find('java')
    assert myfunc('python', sentence) == sentence.find('python')
    assert myfunc('language', sentence) == sentence.find('language')
