#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function accepts INTEGER_ARRAY numbers as parameter.
#
from collections import defaultdict


def closestNumbers(numbers):
    numbers.sort()
    min_diff = float("inf")
    for i in range(len(numbers) - 1):
        min_diff = min(numbers[i + 1] - numbers[i], min_diff)

    for i in range(len(numbers) - 1):
        curr_num = numbers[i]
        next_num = numbers[i + 1]
        if next_num - curr_num == min_diff:
            print(curr_num, next_num)


if __name__ == "__main__":
    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    closestNumbers(numbers)
