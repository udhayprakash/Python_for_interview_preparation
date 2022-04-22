#!/usr/bin/python3


def sum_of_digits(number):
    summation = 0
    while number:
        summation += number % 10
        number //= 10
    return summation


def solution(A):  # O(n^2)
    sums = {}
    for index1, num1 in enumerate(A):
        for index2, num2 in enumerate(A):
            if index1 != index2 and sum_of_digits(num1) == sum_of_digits(num2):
                digits_sum = sum_of_digits(num1)
                sums.setdefault(digits_sum, 0)
                curr_sum = num1 + num2
                if curr_sum > sums[digits_sum]:
                    sums[digits_sum] = curr_sum
    return max(sums.values()) if sums else -1


print(solution([10, 20]))


def solution(A):  # O(n)
    sums = {}
    for num in A:
        digits_sum = sum_of_digits(num)
        sums.setdefault(digits_sum, [])
        sums[digits_sum].append(num)

    max_sum = float("-inf")
    for nums in sums.values():
        curr_sum = sum(nums)
        if curr_sum > max_sum:
            max_sum = curr_sum
    return -1 if max_sum == float("-inf") else max_sum


print(solution([10, 20]))
