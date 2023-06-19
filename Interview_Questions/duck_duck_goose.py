"""
Problem: duck, duck, goose

    write a function that accepts a list of numbers
        - goose: any number divisable by 7 without a remainder
        - duck: any number not a goose

    if duck, move the same number of spots as that numbers value
    if goose, end.
    if you go around the list more than 2 times, you are now a goose.

    always print out "value: type"

"""

from typing import Tuple


def myfunction(numbers: Tuple[int]):
    loopStartcount = 0
    i = 0
    while i < len(numbers):
        if i == 0:
            loopStartcount += 1
        if loopStartcount == 3:
            print(f"7: goose")
            break

        num = numbers[i]
        if num % 7 == 0:
            print(f"{num}: goose")
            break

        print(f"{num}: duck", end=",")
        i += num


myfunction((3, 3, 7, -1))
# 3: duck, -1: duck, 7: goose

myfunction((21, 5, 0))
# 21: goose

myfunction((1, 1, 1, -3))
# 1: duck, 1: duck, 1: duck, -3: duck
# (2nd pass) 1: duck, 1: duck, 1: duck, -3: duck
# (3rd pass) # (7,1,1,-3). 7: goose
