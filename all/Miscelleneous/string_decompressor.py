#!/usr/bin/python
"""
Purpose:
"""


def decompressor(input_str):
    output_str = ""
    digits = ""
    for each_chr in input_str:
        if each_chr in "0123456789":
            digits += each_chr
        else:
            if digits:
                output_str = output_str[:-1] + output_str[-1] * int(digits)
            output_str += each_chr
            digits = ""
    return output_str


if __name__ == "__main__":
    assert decompressor("ab3c4d10a") == "abbbccccdddddddddda"
