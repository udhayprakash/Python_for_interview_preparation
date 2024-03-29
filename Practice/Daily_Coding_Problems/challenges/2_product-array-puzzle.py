"""
#2
Uber

Given an array of integers, return a new array such that each element at index i of the new array is the product of
all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

"""


def bruteforce(arr):
    l = len(arr)
    prod = []
    for i in range(l):
        product = 1
        for j in range(l):
            if i != j:
                product *= arr[j]
        prod.append(product)
    return prod


def bruteforce2(arr):
    # O(n * (n-1))
    new_list = []
    for _index, _ in enumerate(arr):
        product = 1
        for each in arr[:_index] + arr[_index + 1 :]:
            product *= each
        new_list.append(product)
    return new_list


def usingDivision(arr):
    product = 1
    for number in arr:
        product *= number

    prod = [product // x for x in arr]
    return prod


def withoutdivision(arr):
    l = len(arr)
    left = [1 for _ in range(l)]
    right = [1 for _ in range(l)]
    prod = [1 for _ in range(l)]

    for i in range(1, l):
        left[i] = arr[i - 1] * left[i - 1]

    for i in range(l - 2, -1, -1):
        right[i] = arr[i + 1] * right[i + 1]

    for i in range(l):
        prod[i] = left[i] * right[i]

    return prod


if __name__ == "__main__":
    assert bruteforce([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert bruteforce2([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert usingDivision([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert withoutdivision([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
