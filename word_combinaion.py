#!/usr/bin/python3
"""
Write a function that given an integer "N" and a
list of words "A" return all words of length "N" from "A"
that are made of the concatenation of two words from "A"
e.g. N=6, A=[hot, bird, dog, tailor, hotdog, or, if, tail]
--> (tailor = tail+or, hotdog = hot+dog)
"""
from collections import defaultdict

def word_combinations(A, N):
    """ Method 1 - brute force method - O(n^2)"""
    combinations = set()
    for word1 in A:
        for word2 in A:
            if word1 + word2 in A:
                combinations.add(word1 + word2)
    return sorted(combinations)

def word_combinations(A, N):
    """ Method 2 -O(nm)"""
    processed = defaultdict(list)
    for word in A:
        processed[len(word)].append(word)

    combinations = set()
    for p_wordlen, p_words in processed.items():
        if p_wordlen == N:
            combinations.update(p_words)
        else:
            remlen = N - p_wordlen
            if not remlen in processed:
                continue
            for wd1 in p_words:
                for wd2 in processed[remlen]:
                    if wd1 + wd2 in A:
                        combinations.add(wd1 + wd2)
    return sorted(combinations)


if __name__ == '__main__':
    given_words = ['hot', 'bird', 'dog',
                   'tailor', 'hotdog', 'or', 'if', 'tail']
    assert word_combinations(given_words,  0) == []
    assert word_combinations(given_words,  1) == []
    assert word_combinations(given_words,  2) == ['if', 'or']
    assert word_combinations(given_words,  3) == ['dog', 'hot']
    assert word_combinations(given_words,  4) == ['bird', 'tail']
    assert word_combinations(given_words,  5) == []
    assert word_combinations(given_words, 6) == ['hotdog', 'tailor']
    
    assert word_combinations(['a', 'p', 'ap'], 2) == ['ap']
