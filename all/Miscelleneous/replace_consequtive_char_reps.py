#!/usr/bin/python
"""
Purpose: To replace the consequtive repetitive characters
 in the given sentence
"""


def replace_cons_reps(sentence):
    result_str = ''
    for _index, char in enumerate(sentence):
        if _index and sentence[_index] == sentence[_index - 1]:
            continue
        result_str += char
    return result_str


if __name__ == '__main__':
    assert replace_cons_reps('Seeking good work') == 'Seking god work'
    assert replace_cons_reps('Apple fruit') == 'Aple fruit'
