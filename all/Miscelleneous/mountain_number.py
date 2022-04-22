#!/usr/bin/python3
"""
Problem: A mountain number is a number which has the following definitions:
    1. The number must start and end at the same height - 12321 is valid but 123432 is not.
    2. The number has a single 'peak' digit - '5' is the peak for 134521.
    3. It does not have to start (and end) at 1 - 236862 is valid.
    4. It does not contain any local peaks - the digits before the ultimate peak are always increasing
and after the peak are always decreasing - 1324311 is not a valid mountain as 2<3 and 1=1.
Task:
    Write code which will represent and validate a mountain number. It should:
        • Accept a number from the terminal to validate and print 'true' or 'false' if the number is or is not
        a mountain number.
        • Accept a delimited list of numbers and return a delimited list of results.
        • Use object-oriented code appropriately.
        • Have at least 1 unit test.
        • Have clear comments, including parameter typing and return types for functions/methods.
        • Follow PEP8 guidelines.
        • Work on Python 3.9.
        • Include a requirements file.

"""


def is_mountain_number(number):
    if number < 0:
        return False
    elif 0 <= number <= 9:
        return True

    number = str(number)

    # No single peak -- all same
    if len(set(number)) == 1:
        return False

    # number must start & end at same height
    if number[0] != number[-1]:
        return False

    prev_digit = number[0]
    peak_found = False
    for curr_digit in number[1:]:
        # print(f'{number} {prev_digit=} {curr_digit=}')
        if peak_found:
            if prev_digit < curr_digit:
                return False
        else:
            if prev_digit >= curr_digit:
                peak_found = True
        prev_digit = curr_digit
    return True


if __name__ == "__main__":
    assert is_mountain_number(-1) is False
    assert is_mountain_number(-121) is False
    assert is_mountain_number(0) is True
    assert is_mountain_number(8) is True
    assert is_mountain_number(888) is False, "No single peak"
    assert is_mountain_number(5555555555555) is False, "No single peak"
    assert is_mountain_number(236862) is True, "Need not start/end with 1"
    assert is_mountain_number(12) is False, "start & end not same height"
    assert is_mountain_number(122) is False, "start & end not same height"
    assert is_mountain_number(121) is True
    assert is_mountain_number(12321) is True
    assert is_mountain_number(123432) is False
    assert is_mountain_number(134521) is True
