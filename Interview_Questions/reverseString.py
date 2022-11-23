def reverseStringFunc(word):
    revstr = ""
    strlne = len(word)
    for i in range(strlne):
        revstr += word[strlne - i - 1]
    return revstr

    O(n)


def reverseStringFunc(word):
    revstr = ""
    for ch in word:  # O(n)
        revstr = ch + revstr
    return revstr


def reverseStringFunc(word):
    word = list(word)
    strlen = len(word)
    for i in range(strlen // 2):
        word[i], word[strlen - i - 1] = word[strlen - i - 1], word[i]
    return "".join(word)


def reverseStringFunc(word):
    if not word:
        return ""
    return reverseStringFunc(word[1:]) + word[0]
