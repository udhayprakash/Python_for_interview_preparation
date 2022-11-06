# Roman numerals are represented by several different symbols including: I, V, X, L, C, D, M, ↁ.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# ↁ             5000

# For example, 2 is written as II in Roman numeral,
# just two one's added together. 12 is written as XII, which is simply X + II.
# The number 27 is written as XXVII, which is XX + V + II.

# Some rules that indicate a valid roman numeral include:
# 1. Roman numerals are usually written largest to smallest from left to right.
# 2. It is to be noted that no Roman numerals can come together more than 3 times
#    Eg: The numeral for four is not IIII, it's IV.
#    In those cases we use a smaller number before a bigger number to represent the value
#    subtracting the smaller number from the bigger number.
#    9 follows the same principle, its written IX
#    The remaining valid characters (40, 90, 400, 900, 4000) follow the same   pattern.
# 3: The letters V, L, and D are not repeated.

# Please write a python implementation to determine if a string of characters is a valid
# roman number. Please have the program provide informative error messages to the user to describe
# how the string is an invalid roman numeral


# Sample Inputs

valid_list = ["XX", "XXX", "MMXXII", "IV", "MMCDXL", "Mↁ"]
invalid_list = ["alphabet", "IIV", "IIII", "VV", "XX11XX", "XXIXXIIII", "VVVCCXXVV"]


def is_roman(input_string):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "ↁ": 5000,
    }
    str_len = len(input_string)
    final_value = 0
    prev_value = 0
    for index, _ in enumerate(input_string):
        eachchr = input_string[str_len - 1 - index]
        curr_value = values.get(eachchr)
        if not curr_value:
            # print("===", input_string, prev_value, curr_value)
            return "Invalid"
        if prev_value <= curr_value:
            final_value += curr_value
        else:
            final_value -= curr_value
        print("input-_string", input_string, "prev", prev_value, "curr", curr_value)
        prev_value = curr_value
    return "Valid" if final_value else "Invalid"

    return "Valid"


print("Is Roman:")
for sample in valid_list:
    print(is_roman(sample))
print("------------------------")
print("Not Roman")
for sample in invalid_list:
    print(is_roman(sample))
