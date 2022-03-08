#!/usr/bin/python3
"""
Purpose: Display prime numbers, below a given number
"""
import time


def time_taken(func):
    def inner(*args, **kwargs):
        start = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end = time.perf_counter_ns()
        print(f'\nTIME TAKEN: {end- start} nano seconds')
        return result
    return inner


@time_taken
def primes_below(number):
    primes = []
    for num in range(2, number):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes

print(primes_below(10))
print(primes_below(100))

@time_taken
def primes_below(number):
    primes = []
    for num in range(2, number):
        for i in primes:
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes

print(primes_below(10))
print(primes_below(100))


@time_taken
def primes_below(number):
    primes = {}
    for num in range(2, number):
        for i in primes:
            if num % i == 0:
                break
        else:
            primes[num] = 0
    return primes.keys()

print(primes_below(10))
print(primes_below(100))
