def findCompletePrefixes(names, query):
    prefix_freq = {}
    for query_word in query:
        prefix_freq.setdefault(query_word, 0)
        for name in names:
            if name.startswith(query_word):
                if name == query_word:
                    continue
                prefix_freq[query_word] += 1

    return list(prefix_freq.values())


names1 = ['steve', 'stevens', 'danny', 'steves', 'dan',
          'john', 'johnny', 'joe', 'alex', 'alexander']
query1 = ['steve', 'alex', 'joe', 'john', 'dan']
print(findCompletePrefixes(names1, query1) == [2, 1, 0, 1, 1])
