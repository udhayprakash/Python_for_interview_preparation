#!/usr/bin/python3
"""
Problem: Given a number, create a maximum & minimum
  numbers, using its digits and get the difference
  between maximum and minimum numbers.
"""


def comp_diff(num):
    digits = list(str(num))
    digits.sort()
    minVal = ''.join(digits)
    maxVal = minVal[::-1]
    print(minVal, maxVal)
    return int(maxVal) - int(minVal)


print(comp_diff(213))


def comp_diff(num):
    digits = []
    while num:
        digits.append(num % 10)
        num //= 10
    digits.sort()  # [1, 2, 3]
    minVal, maxVal = 0, 0
    digitsCount = len(digits)
    for index, digit in enumerate(digits):
        maxVal += digit * (10 ** index)  # 0, 1, 2
        minVal += digit * (10 ** (digitsCount - index - 1))
    print(minVal, maxVal)
    return maxVal - minVal


print(comp_diff(213))
