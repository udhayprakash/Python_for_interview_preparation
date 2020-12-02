#!/usr/bin/python
"""
Purpose: 
"""
from collections import defaultdict
from pprint import pprint

# def get_anagrams(given_words):
#     sorted_words = {''.join(sorted(word.lower())) for word in given_words}
#     print('sorted_words', sorted_words)
#     result = {}
#     for word in given_words:
#         anagram_word = ''.join(sorted(word.lower()))
#         print('anagram_word', anagram_word)
#         if anagram_word in sorted_words:
#             result[anagram_word] = result.get(anagram_word, []).append(word)
#     print(result)
#     return []


def get_anagrams(given_words):
    result = defaultdict(list)
    for word in given_words:
        result[''.join(sorted(word.lower()))].append(word)

    return [v for v in result.values() if len(v) > 1]


if __name__ == '__main__':
    assert get_anagrams(['Eat', 'Ate', 'Tea', 'Boy', 'Girl']) == [
        ['Eat', 'Ate', 'Tea']]
    assert get_anagrams(['Eat', 'Ate', 'Girl', 'Girl']) == [
        ['Eat', 'Ate', 'Tea']]
    # assert get_anagrams(['Eat', 'Ate', 'Tea', 'Boy', 'Girl']) == [['Eat', 'Ate', 'Tea']]


def get_anagrams(given_words):
    result = defaultdict(list)
    for word in given_words:
        result[''.join(sorted(word.lower()))].append(word)
    return [v for k, v in result.items()]


words = ['Eat', 'Ate', 'Girl', 'Girl']
print(get_anagrams(words))
assert get_anagrams(words) == [set(['Ate', 'Eat'])]

words = ['Eat', 'Ate', 'Ate', 'Girl', 'Girl']
assert get_anagrams(words) == [set(['Ate', 'Eat'], set('Girl'))]
