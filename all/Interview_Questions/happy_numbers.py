# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a
# cycle which does not include 1. Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not. Constraints: 1 <= n <= 2^31 - 1
# Example 1:
#     Input: n = 19
#     Output: true
# Explanation: 1^2 + 9^2 = 82
#              8^2 + 2^2 = 68
#              6^2 + 8^2 = 100
#              1^2 + 0^2 + 0^2 = 1
# Example 2:
#     Input: n = 2
#     Output: false
# Explanation : 2^2 = 4
#             4^2 = 16
# 1^2 + 6^2 = 37 3^2 + 7^2 = 58 5^2 + 8^2 = 89 8^2 + 9^2 = 145 1^2 + 4^2 + 5^2 = 42 4^2 + 2^2 = 20 2^2 + 0^2 = 4


def ishappy(num, processed_results=None):
    # print(f'num= {num}')
    if not processed_results:
        processed_results = []
    squaresum = 0
    while num:
        squaresum += (num % 10) ** 2
        num //= 10
    if squaresum == 1:
        return "happy"
    elif squaresum in processed_results:
        return "unhappy"
    processed_results.append(squaresum)
    return ishappy(squaresum, processed_results)


print("ishappy(193)", ishappy(193))
print("ishappy(2)", ishappy(2))
