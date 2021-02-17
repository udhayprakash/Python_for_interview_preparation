#!/usr/bin/python
"""
Purpose: Write a program that prints the numbers from 1 to 100.
But, for multiples of three print 'Fizz' instead of number and 
for multiples of five print 'Buzz'. For numbers which are multiples
of both three and five, print 'FizzBuzz'.
"""


def fizz_buzz(n):
    for i in range(1, n + 1):
        result = ''
        if i % 3 == 0:
            result += 'Fizz'
        if i % 5 == 0:
            result += 'Buzz'

        print(result if result else i)


if __name__ == '__main__':
    fizz_buzz(15)
