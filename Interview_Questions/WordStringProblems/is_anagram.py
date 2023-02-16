def is_anagram(str1, str2):
    if str1 == str2:
        return True
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)


def is_anagram(str1, str2):

    if len(str1) != len(str2):
        return False

    str1_count = sum([ord(each1) for each1 in str1])
    str2_count = sum([ord(each2) for each2 in str2])

    return str1_count == str2_count


def is_anagram(str1, str2):
    str1_dict = {}
    for ch in str1:
        str1_dict.setdefault(ch, 0)
        str1_dict[ch] += 1
    for ch in str2:
        freq = str1_dict.get(ch, 0)
        if not freq:
            return False
        str1_dict[ch] -= 1
    for ch, frq in str1_dict.items():
        if frq != 0:
            return False
    return True


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
