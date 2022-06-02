# /usr/bin/python
"""
Geometric Series:
    1 + x + x ^ 2 + x ^ 3 + x ^4  ..... + x ^ n = (x^(n+1) - 1)/(x - 1) for x != 1
"""

import time

# Method 1
start_time = time.perf_counter()
result = (
    (2 ^ 0)
    + (2 ^ 1)
    + (2 ^ 2)
    + (2 ^ 3)
    + (2 ^ 4)
    + (2 ^ 5)
    + (2 ^ 6)
    + (2 ^ 7)
    + (2 ^ 8)
    + (2 ^ 9)
    + (2 ^ 10)
)
print(f"{result =}")
print(f"TIME TAKEN : {time.perf_counter() - start_time}")


print()
# Method 2
start_time = time.perf_counter()
result = (2 ^ (10 + 1) - 1) / (2 - 1)  # x = 2 & n = 10
print(f"{result =}")
print(f"TIME TAKEN : {time.perf_counter() - start_time}")
