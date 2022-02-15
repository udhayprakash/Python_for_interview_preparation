#!/usr/bin/python
"""
Problem: https://www.codechef.com/problems/CHEFDIL
"""

# 1 - up , 0 - down

replace = {
    '0': '1',
    '1': '0'
}


def myfunc(testString):  # testString = '10'
    ts = list(testString)  # ['1', '0']

    i = 0
    while i < len(ts):
        if ts[i] == '0':
            i += 1
        else:
            if i-1 >= 0:  # before
                ts[i-1] = replace[ts[i-1]]
            try:
                ts[i+1] = replace[ts[i+1]]
            except IndexError:
                pass
            del ts[i]

    return 'LOSE' if ts else 'WIN'


assert myfunc('10') == 'WIN'
assert myfunc('10100') == 'LOSE'
assert myfunc('101') == 'LOSE'

print(myfunc('1010011100001'))



