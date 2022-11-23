"""
Problem: Meta Interview Question

    Check if string is a valid number
    Given a  string, write a method that returns true if the
    string is a valid number or false otherwise.

    Only integers and decimals should be considered as valid.
    In other words, only characters allowed are digits, "-" and ".".

    The string can be very long (think millions of characters) and
    no built-in function/class can handle it without overflowing
    or losing precision.

Some example strings and expected output:

    | Input  | Output |
    | -----  | -----  |
    | "13"   | TRUE   |
    | "3.0"  | TRUE   |
    | "-7.4" | TRUE   |
    | "abc"  | FALSE  |
    | "123a" | FALSE  |

"192.168.0.1" FALSE
"-" FALSE
"-." FALSE
"-23.983"
"""
# def validator(givenStr):
#     return True if givenStr.isdigit() else False


# dict -- o(1)
import re


def validator(givenStr):
    # striiped  prependng '0' and white space and negative sign
    givenStr = givenStr.lstrip("0 ")

    dotCount = 0
    digitPresent = False
    # eachCHar == '3'
    for index, eachChar in enumerate(givenStr):
        if index == 0 and eachChar == "-":  # for -ve sign
            continue
        elif eachChar == ".":
            if dotCount == 0:
                dotCount += 1
                continue
            else:
                return False

        elif not re.findall("[0-9]", eachChar):  # not True -> False
            return False
        else:
            digitPresent = True  # digitPresenr = True
    return True if digitPresent else False  # True


assert validator("13") is True
assert validator("000013") is True

assert validator("abc") is False
assert validator("123a") is False


assert validator("3.0") is True
assert validator("3.") is True
assert validator(".3") is True

assert validator("..3") is False
assert validator(".3.") is False
assert validator("3..") is False
assert validator("3.4.") is False
assert validator("3.4.5") is False


# - ve sign should be only at the start of it
assert validator("-7.4") is True
assert validator("7-.4") is False
assert validator("7.4-") is False

assert validator("-") is False
assert validator(".") is False


assert validator("         -7.4") is True
assert validator("-7     .4") is False
