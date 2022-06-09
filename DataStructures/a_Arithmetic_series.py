#!/usr/bin/python
"""
Purpose" Arithmecti Series  - n*(n +1)/2
"""
import time

# Method 1
start_time = time.perf_counter()
result = (
    1
    + 2
    + 3
    + 4
    + 5
    + 6
    + 7
    + 8
    + 9
    + 10
    + 11
    + 12
    + 13
    + 14
    + 15
    + 16
    + 17
    + 18
    + 19
    + 20
    + 21
    + 22
    + 23
    + 24
    + 25
    + 26
    + 27
    + 28
    + 29
    + 30
    + 31
    + 32
    + 33
    + 34
    + 35
    + 36
    + 37
    + 38
)
print(f"{result =}")
print(f"TIME TAKEN : {time.perf_counter() - start_time}")


print()
# Method 2
start_time = time.perf_counter()
result = (38 * (38 + 1)) / 2
print(f"{result =}")
print(f"TIME TAKEN : {time.perf_counter() - start_time}")

# conclusion : use formulae for large values summation
# that too if the nums are not missing any value in sequence
