from collections import defaultdict


def group_anagrams(words):
    result = defaultdict(list)
    for word in words:
        result[str(sorted(word))].append(word)
    return list(result.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams(["act", "tac", "cat", "shad", "dash"]))


def group_anagrams(words):
    result = {}
    for word in words:
        sorted_word_str = str(sorted(word))
        result.setdefault(sorted_word_str, [])
        result[sorted_word_str].append(word)
    return list(result.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams(["act", "tac", "cat", "shad", "dash"]))
