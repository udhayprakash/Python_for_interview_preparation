#!/usr/bin/python3
"""
Purpose: String Replace 

"""


def string_replace(given_str):
    words = given_str.split()
    max_len, max_len_index = 0, 0
    for index, word in enumerate(words):
        word = word[0].upper() + word[1:]
        words[index] = word
        word_len = len(word)
        if word_len > max_len:
            max_len = word_len
            max_len_index = index
    words[max_len_index] = words[max_len_index].upper()

    return ' '.join(words)



inputStr = "Adnan and Omkar are having discussion for a python developer role opportunity in nitor"
expectedStr = "Adnan And Omkar Are Having Discussion For A Python Developer Role OPPORTUNITY In Nitor"
assert string_replace(inputStr) == expectedStr
