"""
Problem: Given two strings. The task is to check whether the given strings are anagrams of each other or not without using any sort function
An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, “abcd” and “dabc” are an anagram of each other.

    Input: str1 = “listen”  str2 = “silent”
    Output: “Anagram”
    Explanation: All characters of “listen” and “silent” are the same.


    Input: str1 = “gram”  str2 = “arm”
    Output: “Not Anagram”

"""


def is_anagram(str1, str2):
    if str1 == str2:
        return True
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)


def is_anagram(s, t):
    if s == t:
        return True
    if len(s) != len(t):
        return False

    str1_dict = {}
    for ch in s:
        str1_dict.setdefault(ch, 0)
        str1_dict[ch] += 1
    for ch in t:
        freq = str1_dict.get(ch, 0)
        if not freq:
            return False
        str1_dict[ch] -= 1
    for frq in str1_dict.values():
        if frq != 0:
            return False
    return True


def is_anagram(s, t):
    counter_s = [0] * 26
    counter_t = [0] * 26

    for char in s:
        counter_s[ord(char) - 97] += 1  # ord("a") is ord('a')

    for char in t:
        counter_t[ord(char) - 97] += 1

    return counter_s == counter_t


if __name__ == "__main__":
    assert is_anagram("abcd", "cdab") is True
    assert is_anagram("aabfffr", "afbfraf") is True

    assert is_anagram("kdkd", "dkdr") is False
    assert is_anagram("kdkd", "dkkd") is True

    def test():
        testcases = [
            ("listen", "silent", True),
            ("dad", "bad", False),
            ("test", "test", True),
            ("test", "tests", False),
            ("bad", "dad", False),
            ("listens", "enlists", True),
            ("listens", "enlist", False),
            ("elbow", "below", True),
        ]
        for s1, s2, result in testcases:
            assert is_anagram(s1, s2) == result

    test()
