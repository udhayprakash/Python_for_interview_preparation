#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'carParkingRoof' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY cars
#  2. INTEGER k
#


def carParkingRoof(cars, k):
    l = len(cars)
    if l == 0 or k == 0:
        return 0
    cars.sort()

    res = float("inf")
    for i in range(l):
        if i >= (k - 1):
            res = min(res, cars[i] - cars[i - (k - 1)])
    print(res)
    return res + 1


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    cars_count = int(input().strip())

    cars = []

    for _ in range(cars_count):
        cars_item = int(input().strip())
        cars.append(cars_item)

    k = int(input().strip())

    result = carParkingRoof(cars, k)

    fptr.write(str(result) + "\n")

    fptr.close()
