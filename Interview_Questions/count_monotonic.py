"""
Create a function to count the number of monotonic sub-sequences in an array.
 A monotonic sequence has either increasing or decreasing integers.
Example: count_monotonic([1, 3, 5, 7, 4, 3, 2, 5, 6, 8]) —> 3
"""


def are_both_opposite_sign(n1, n2):
    return (n1 ^ n2) < 0


def count_monotonic(given_list):
    if not given_list:
        return 0

    sequences_count = 1
    if len(given_list) <= 2:
        return sequences_count

    prev_diff = 0
    constant_tonic = False
    for index, num in enumerate(given_list):
        if index == 0:
            continue
        if num == given_list[index - 1]:  # constant
            if constant_tonic is False:
                constant_tonic = True
                sequences_count += 1
                print(given_list[:index])
        else:
            constant_tonic = False
            curr_diff = num - given_list[index - 1]
            if are_both_opposite_sign(prev_diff, curr_diff):  # increasing/decreasing
                sequences_count += 1
                print(given_list[:index])
        prev_diff = curr_diff

    return sequences_count


assert count_monotonic([]) == 0
assert count_monotonic([1]) == 1
assert count_monotonic([1, 3]) == 1
assert count_monotonic([3, 1]) == 1
assert count_monotonic([1, 3, 5, 7]) == 1
assert count_monotonic([1, 3, 5, 7, 4, 3, 2]) == 2
assert count_monotonic([1, 3, 5, 7, 4, 3, 2, 5]) == 3
assert count_monotonic([1, 3, 5, 7, 4, 3, 2, 5, 6, 8]) == 3
assert count_monotonic([1, 3, 5, 7, 4, 3, 2, 5, 6, 8, 8]) == 4
assert count_monotonic([1, 3, 5, 7, 4, 3, 2, 8, 8, 8, 8]) == 4
assert count_monotonic([1, 3, 5, 7, 4, 3, 2, 5, 8, 8, 8, 5]) == 5
