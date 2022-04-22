#!/usr/bin/python3
"""
Purpose: For the given string, find the
        smallest palindrome substring
"""


def is_palindrome(given_str):
    return given_str == given_str[::-1]


def is_palindrome(given_str):
    for index in range(len(given_str) // 2):
        if given_str[index] != given_str[-index - 1]:
            return False
    return True


def get_smallest_palindrome(given_string):
    pass


if __name__ == "__main__":
    # get_smallest_palindrome('nitin')
    get_smallest_palindrome("microsoft")
#         t
#        ft
#       oft
#      soft
#     osoft
#    rosoft
#   crosoft
#  icrosoft
# microsoft
# microsof
# microso
# micros
# micro
# micr
# mic
# mi
# m

# microsoft
# icrosof
