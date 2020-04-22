#!/usr/bin/python
"""
Purpose: Balancing braces in expression
    Given a string, parse if the bracets are ending correctly
        {}, (), []
"""
__name__ = 'Author'

braces = {
    '}': '{',
    ')': '(',
    ']': '['
}


def check_braces_balance(expression):
    braces_found = []
    for each_chr in expression:
        if each_chr in '{([':
            braces_found.append(each_chr)
        elif each_chr in '})]':
            if ((not braces_found) or
                    braces_found[-1] != braces[each_chr]):
                return False
            braces_found.pop()
    return True


if __name__ == '__main__':
    assert check_braces_balance('sdjf{[df]}()') is True
    assert check_braces_balance('sdjf{[d)f]})()') is False
    assert check_braces_balance('sdjf{[d()f]})()') is False
    assert check_braces_balance('sdjf{[d()f]}()') is True
