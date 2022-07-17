# Double letters:

# The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

# Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.


def double_letters(word):
    # if string is empty
    if not word:
        return False

    word_len = len(word)
    # if string contains only one character
    if word_len == 1:
        return False

    i = 1
    while i < word_len:
        if word[i - 1] == word[i]:  # comparing prev & curr characters
            return True
        i += 1
    return False


assert double_letters("hello") is True
assert double_letters("nono") is False

assert double_letters("app") is True
assert double_letters("apple") is True
assert double_letters("am11") is True
assert double_letters("am") is False
assert double_letters("a") is False
assert double_letters("1") is False

assert double_letters("") is False
assert double_letters("  ") is True
assert double_letters("--") is True
