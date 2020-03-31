#!/usr/bin/python
"""
Purpose: https://www.geeksforgeeks.org/given-array-strings-find-strings-can-chained-form-circle/
"""
def are_words_chainable(given_words):
    given_words.sort()
    chained_words = [given_words[0]]
    for _index, given_word in enumerate(given_words):
        if (_index 
            and given_word[0] == chained_words[-1][-1]): 
    print(chained_words)
    return True


if __name__ == '__main__':
    assert are_words_chainable(["for", "geek", "rig", "kaf"]) == True
    # assert are_words_chainable(["geek", "king"]) == True
    # assert are_words_chainable(["aab", "bac", "aaa", "cda"]) == True
    # assert are_words_chainable(["aaa", "bbb", "baa", "aab"]) == True
    # assert are_words_chainable(["aaa", "bbb"]) == False
    # assert are_words_chainable(["abc", "efg", "cde", "ghi", "ija"]) == True
    # assert are_words_chainable(["ijk", "kji", "abc", "cba"]) == False
