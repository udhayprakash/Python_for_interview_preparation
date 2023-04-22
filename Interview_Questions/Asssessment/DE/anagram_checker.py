""""
Problem:
    Anagram is a word, phrase, or name formed by rearranging the letters of another.
    For example: Silent is an Anagram of Listen.

    Write an example program that determines if a pair of words are Anagrams.
"""


def is_anagram(word1, word2):
    # convert to lowercase for case-insensitive comparison
    # removing white spaces anywhere in the string
    word1 = word1.strip().replace(" ", "").lower()
    word2 = word2.strip().replace(" ", "").lower()
    return sorted(word1) == sorted(word2)


if __name__ == "__main__":
    # Case 1: Same words
    assert is_anagram("listen", "silent") == True
    assert is_anagram("Hello", "llohe") == True
    assert is_anagram("Anagram", "NAGRAMA") == True

    # Case 2: Different words
    assert is_anagram("python", "java") == False
    assert is_anagram("world", "hello") == False
    assert is_anagram("abcd", "efgh") == False

    # Case 3: Empty strings
    assert is_anagram("", "") == True

    # Case 4: Single character words
    assert is_anagram("a", "a") == True
    assert is_anagram("a", "b") == False

    # Case 5: Words with whitespace
    assert is_anagram("word", "dow r") == True
    assert is_anagram("spaces", "s p aces") == True

    # Case 6: Words with special characters
    assert is_anagram("word!", "!dorw") == True
    assert is_anagram("python", "Java") == False

    # Case 7: Words with numbers
    assert is_anagram("12345", "54321") == True
    assert is_anagram("98765", "56789") == True
