#!/usr/bin/python3
"""
Purpose: Parsing string
"""
def string_parser(givStr, limit):
    result = {v.split(':')[0] for v in givStr.replace('%', ':').split(',')
              if int(v.split(':')[1]) <= limit}
    return sorted(result)


print(string_parser("A%3,B%4,C%2,D:1,E:3,F:6", 3))
