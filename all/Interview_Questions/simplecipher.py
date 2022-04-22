#!/usr/bin/python3
"""
Purpose:
"""


def simpleCipher(encrypted, k):
    k = k % 26
    res = ""
    for e in encrypted:
        c = ord(e)
        if chr(c - k) < "A":
            res += chr(c - k * 26)
        else:
            res += chr(c - k)
    return res


if __name__ == "__main__":
    assert simpleCipher("CDEF", 2) == "ABCD"
    assert simpleCipher("cdef", 2) == "abcd"
    assert simpleCipher("", 2) == ""
    print(simpleCipher("xyz", 2))  # vwx
    print(simpleCipher("abc", 2))  # vwx
