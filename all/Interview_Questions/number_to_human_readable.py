#!/usr/bin/python3
"""
Purpose: Number to Human readable
"""
num_words = {
    0: 'ZERO',
    1: 'ONE',
    2: 'TWO',
    3: 'THREE',
    4: 'FOUR',
    5: 'FIVE',
    6: 'SIX',
    7: 'SEVEN',
    8: 'EIGHT',
    9: 'NINE'
}
place_values = {
    1: 'ones',
    2: 'tens',
    3: 'hundred',
    4: 'thousand',
    5: 'ten thousand',
    6: 'lack'
}


def human_readable(num):
    num_str = ''
    count = 1
    while num:
        digit = num % 10
        num_str += ' ' + num_words[digit] + ' ' + place_values[count]
        num //= 10
        count += 1
    return num_str


print(human_readable(345))
