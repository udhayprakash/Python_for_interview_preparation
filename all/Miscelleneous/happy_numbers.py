#!/usr/bin/python3

N = 6
K= 3
given_array = [5, 5, 7, 9, 15, 2]

happy_numbers = 0
for x in given_array:
    for i in range(x-3, x+3):
        if x != i and i in given_array:
            happy_numbers += 1
            break
print(f'{happy_numbers =}')