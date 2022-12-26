def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    str1_count = sum([ord(each1) for each1 in str1])
    str2_count = sum([ord(each2) for each2 in str2])

    return str1_count == str2_count


assert is_anagram("abcd", "cdab") is True
assert is_anagram("aabfffr", "afbfraf") is True

assert is_anagram("kdkd", "dkdr") is False
assert is_anagram("kdkd", "dkkd") is True
