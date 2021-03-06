#!/usr/bin/python
"""
Purpose: Find the longest palindrome substring in the given string 

"""


def find_longest_substring(given_string):
    if given_string == given_string[::-1]:
        return given_string
    else:
        longest_palindrome = ''
        for _index, _ in enumerate(given_string):
            sub_str = given_string[_index:]
            for _index2, _ in enumerate(sub_str[::-1]):
                sub_str2 = sub_str[::-1][_index2:]
                if sub_str2 == sub_str2[::-1] and len(sub_str2) > len(longest_palindrome):
                    longest_palindrome = sub_str2
        return longest_palindrome



def get_prefixes_of_string(given_string):
    lg_prefix_lengths = []
    for index, _ in enumerate(given_string):
        lg_pal_str = find_longest_substring(given_string[index:])
        lg_prefix_lengths.append(len(lg_pal_str))
        # print(f'{given_string[index:]:7} ==>{len(lg_pal_str)} {lg_pal_str}')
    return sorted(lg_prefix_lengths)

assert get_prefixes_of_string("ababa") == [1, 1, 3, 3, 5]