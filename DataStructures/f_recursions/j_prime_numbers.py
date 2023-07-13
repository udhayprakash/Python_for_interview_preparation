#!/usr/bin/python
"""
Purpose: prime number check
    2, 3, 5, 7
"""
import time


# Method 1 - using iterations
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            # print(f'\t{i =}')
            return False
    return True


start_time = time.perf_counter_ns()
print(f"{is_prime(13)       =}")
print(f"{is_prime(15)       =}")
print(f"{is_prime(17)       =}")
print(f"{is_prime(31)       =}")
print(f"{is_prime(563)      =}")
print(f"TIME TAKEN:{time.perf_counter_ns() -start_time}")


def is_prime_rec(num, i=2):
    # print(f'\t{num =}, {i=}, {num % i =}')
    if i == num:
        return True
    elif num % i == 0:
        return False
    return is_prime_rec(num, i + 1)


print()
start_time = time.perf_counter_ns()
print(f"{is_prime_rec(13)   =}")
print(f"{is_prime_rec(15)   =}")
print(f"{is_prime_rec(17)   =}")
print(f"{is_prime_rec(31)   =}")
print(f"{is_prime_rec(563)  =}")
print(f"TIME TAKEN:{time.perf_counter_ns() -start_time}")


# NOTE:
# 1. For smaller values, recursion is preferred
# 2. For largers values, iteration is preferred
