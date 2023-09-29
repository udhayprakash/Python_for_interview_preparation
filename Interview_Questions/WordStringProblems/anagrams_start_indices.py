"""
Problem:
    Given two strings s and p,
    an array of all start indices of p's anagrams in s.
    You may return the answer in any order.

Input: s = "kinsininke", p = "nik"
Output: [0,6]

Input: s = "nini", p = "ni
Output: [0,1,2]

kinsininke

kin
 ins
  nsi
   sin
    ini
     ninke

o(nPlogP)

O(N)   == O(N)
    O(1)
"""
# Approach 1
from itertools import permutations
from typing import List, Set


def get_all_anagrams(word: str) -> Set[str]:
    return {"".join(wd_list) for wd_list in permutations(word)}


def start_indices_anagrams(sentence: str, pWord: str) -> List[int]:
    i = 0
    pWord_len = len(pWord)
    pWord_anagrams_set = get_all_anagrams(pWord)  # O()
    start_indices = []
    while i < len(sentence):  # O(N)
        curr_word = sentence[i : i + pWord_len]
        if curr_word in pWord_anagrams_set:  # O(1)
            start_indices.append(i)
        i += 1
    return start_indices


print(start_indices_anagrams("kinsininke", "nik"))
print(start_indices_anagrams("nini", "ni"))
print()

# Approach 2
from collections import Counter


def start_indices_anagrams(sentence: str, pWord: str) -> List[int]:
    pCount = Counter(pWord)  # O(P)
    pWord_len = len(pWord)
    start_indices = []
    for i in range(len(sentence) - pWord_len + 1):  # O(N) = O(NP)
        curr_count = Counter(sentence[i : i + pWord_len])  # O(P)
        if pCount == curr_count:
            start_indices.append(i)
    return start_indices


print(start_indices_anagrams("kinsininke", "nik"))
print(start_indices_anagrams("nini", "ni"))
print()

# Approach 3


def start_indices_anagrams(sentence: str, pWord: str) -> List[int]:  # O(N)
    pCount = Counter(pWord)  # O(P)
    pWord_len = len(pWord)
    start_indices = []

    left, right = 0, pWord_len
    curr_count = Counter(sentence[left:right])

    while right <= len(sentence):  # O(N)
        if pCount == curr_count:
            start_indices.append(left)
        left += 1
        right += 1
        if right <= len(sentence):
            curr_count[sentence[left - 1]] -= 1
            curr_count[sentence[right - 1]] += 1
    return start_indices


print(start_indices_anagrams("kinsininke", "nik"))
print(start_indices_anagrams("nini", "ni"))
