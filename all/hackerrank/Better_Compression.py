#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'betterCompression' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
import re 
def betterCompression(s):
    result = {}
    for char, num in re.findall('([a-zA-Z]+)([0-9]+)', s):
        result.setdefault(char, 0)
        result[char]+= int(num)
    result = sorted(result.items(), key=lambda x:x[0])
    return ''.join(ch + str(n) for ch, n in result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = betterCompression(s)

    fptr.write(result + '\n')

    fptr.close()
