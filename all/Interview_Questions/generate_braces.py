#!/usr/bin/python3
"""
Purpose: Generating Braces 
"""


def genbraces(n):
    result = []
    tempfunc(n, n, "", result)
    return result


def tempfunc(left_brace_count, right_brace_count, brace_str, res):
    if left_brace_count == 0 and right_brace_count == 0:
        res.append(brace_str)
        return
    if left_brace_count > 0:
        tempfunc(left_brace_count-1, right_brace_count, brace_str + '(', res)
    if right_brace_count > left_brace_count:
        tempfunc(left_brace_count, right_brace_count-1, brace_str + ')', res)


# print(genbraces(2))

assert genbraces(2) == ['(())', '()()']
assert genbraces(3) == ['((()))', '(()())', '(())()', '()(())', '()()()']
assert genbraces(4) == ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())',
                        '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', 
                        '()()(())', '()()()()']

