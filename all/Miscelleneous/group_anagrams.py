"""
Group all anagrams together
Anagrams definition: a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman since they have same letters [a, c, e, i, m, n].

Input => ["eat","tea","tan","ate","nat","bat"]
Expected Output => [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

# def group_anagrams(input): # O(n2logn)
#     groups = {}
#     for word in input:  #O(n)
#         word_sorted = ''.join(sorted(word)) # O(nlogn)
#         groups.setdefault(word_sorted, [])
#         groups[word_sorted].append(word) # O(1)
#     return list(groups.values()) # O(n)

def word_sort(wd):  # O(nlogn)
    return ''.join(sorted(wd))


def word_hash(wd):  # O(n)
    char_freq = {}
    for eachChr in wd:   #O(n)
        char_freq.setdefault(eachChr, 0)
        char_freq[eachChr] += 1
    return hash(frozenset(char_freq.items()))  # O(n)

def group_anagrams(input, choice='hash'):
    choices = {
        'hash': word_hash, 
        'sort': word_sort
    }
    user_func = choices.get(choice)
    if not user_func: raise Exception(f'Undefined choice:{choice}')

    groups = {}
    for word in input:  # O(n)
        wrd_hash = user_func(word) 
        groups.setdefault(wrd_hash, [])
        groups[wrd_hash].append(word)  #O(1)
    return list(groups.values())


input = ["eat","tea","tan","ate","nat","bat"]
grouped_result = group_anagrams(input, 'foo')

for group in grouped_result:
    for word in group:
        print(word + ", ")
    print("\n")
