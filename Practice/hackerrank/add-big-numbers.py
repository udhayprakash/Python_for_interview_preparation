#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'addStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING string1
#  2. STRING string2
#


def str2num(numstr):
    nums_map = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    num, count = 0, 0
    while numstr:
        lastChar = numstr[-1]
        # print("\tcount=", count, lastChar, "num1=", numstr)
        if lastChar == ".":
            num = num / (10**count)
            count = 0
        else:
            num += nums_map[lastChar] * (10**count)
            count += 1
        numstr = numstr[:-1]
    return num


def addStrings(string1, string2):
    string1 = string1.strip()
    string2 = string2.strip()
    if not string1:
        return string2
    if not string2:
        return string1

    return str(str2num(string1) + str2num(string2))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    string1 = input()

    string2 = input()

    result = addStrings(string1, string2)

    fptr.write(result + "\n")

    fptr.close()
