def substr_count(given_str: str, substr: str) -> int:
    if not given_str:
        return 0
    if not substr:
        return 0

    substr_count = 0
    substr_len = len(substr)
    i = 0
    while i < len(given_str):
        if given_str[i : i + substr_len] == substr:
            substr_count += 1
        i += 1
    return substr_count


if __name__ == "__main__":
    assert substr_count("", "abc") == 0
    assert substr_count("", "") == 0
    assert substr_count("abc", "") == 0

    assert substr_count("abc", "a") == 1
    assert substr_count("abc", "ab") == 1
    assert substr_count("abc", "abc") == 1
    assert substr_count("abcabc", "abc") == 2
    assert substr_count("abcabcabc", "abc") == 3

    assert substr_count("abcabcabc", "bc") == 3
    assert substr_count("abcabcabc", "c") == 3

    assert substr_count("abcabcabcc", "c") == 4
