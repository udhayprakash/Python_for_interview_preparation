#!/usr/bin/python
"""
Purpose: Converting memory size of human readable format
"""
suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']


def humansize(nbytes):
    i = 0
    while nbytes >= 1024 and i < len(suffixes) - 1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


assert humansize(131) == '131 B'
assert humansize(1049) == '1.02 KB'
assert humansize(58812) == '57.43 KB'
assert humansize(68819826) == '65.63 MB'
assert humansize(39756861649) == '37.03 GB'
assert humansize(18754875155724) == '17.06 TB'
