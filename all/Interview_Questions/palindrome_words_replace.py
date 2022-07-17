"""
Purpose: To find and replace the palindrome words, in sentence,
	in their ascending order
"""


def is_palidrome(wd):
    return wd == wd[::-1]


def myfunc(giveStr):
    words = giveStr.split()
    palWords, palIndices = [], []
    for index, word in enumerate(words):
        if is_palidrome(word):
            palWords.append(word)
            palIndices.append(index)
    palWords.sort()
    for index in palIndices:
        words[index] = palWords.pop(0)
    return " ".join(words)


print(myfunc("Please refer to the madam to know the level"))
