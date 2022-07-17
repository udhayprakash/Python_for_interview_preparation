"""
Purpose: Reverse the digits in a given integer
"""

# def reverse_number(num):
#     return int( str(number)[::-1])


def reverse_number(num):
    digits = []
    placeValue = 0
    while num:
        digit = num % 10
        digits.append(digit)
        num = num // 10
        placeValue += 1
    rev_num = 0
    for index, dg in enumerate(digits):
        rev_num += dg * pow(10, placeValue - index)
    return rev_num


print(reverse_number(12345))
