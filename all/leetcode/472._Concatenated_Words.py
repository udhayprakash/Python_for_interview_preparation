"""
Problem:
    Write a function that given a list of words L and an integer N,
    print the list of words of length N from the list L, made of the
    concatenation of two words from L -
    e.g.
    L=["cat", "dog", "bird", "snow", "snowbird", "tail", "hot", "tailor", "or", "hotdog"]
    and N=6
    ==> hotdog = hot+dog and tailor = tail+or

"""


def myfunc(words, size):
    unique_words = set(words)
    result = []
    for word in words:
        temp = [False] * (len(word) + 1)
        temp[0] = True

        for i, _ in enumerate(word):
            if temp[i] is False:
                continue
            for j in range(i + 1, len(word) + 1):
                if (j - i) < len(word) <= size and word[i:j] in unique_words:
                    temp[j] = True
            if temp[len(word)] is True:
                result.append(word)
                break
    return result


assert myfunc(
    [
        "cat",
        "dog",
        "bird",
        "snow",
        "snowbird",
        "tail",
        "hot",
        "tailor",
        "hotdog",
        "or",
    ],
    6,
) == ["tailor", "hotdog"]
assert myfunc(
    ["cat", "dog", "bird", "snow", "snowbird", "tail", "hot", "tailor", "hotdog"], 6
) == ["hotdog"]
