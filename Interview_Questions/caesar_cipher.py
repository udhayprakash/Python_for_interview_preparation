"""
Caesar's Cipher:
Write the substitution cipher algorithm that shifts all letters in an input string by
a number of positions in the English alphabet.


Example:
    assert cipher("abcdxyz", 5) == "fghicde"

company: squarepoint capital
chr() and ord()
97-122

"""


def cipher(sentence: str, offset: int) -> str:
    encrypted = ""
    offset = offset % 26
    for char in sentence:
        new = ord(char) + offset
        if new > 122:
            new = new - 26
        encrypted += chr(new)
    return encrypted


assert cipher("abcdxyz", 5) == "fghicde"
assert cipher("", 5) == ""
assert cipher("a", 5) == "f"
assert cipher("aaa", 5) == "fff"
assert cipher("zzz", 1) == "aaa"
assert cipher("yy", 2) == "aa"
assert cipher("x", 0) == "x"
assert cipher("x", -1) == "w"
assert cipher("xyzab", -1) == "wxyza"
assert cipher("xyzab", -27) == "wxyza"


assert cipher("x", 3) == "a"  # assert cipher("x", equivalent-of-3) ==  "a"
print("2421 ", cipher("x", 2421))

# print(3, 2421% 26)   # 26*11 + 3 | 26 * 1000 + 3

"""
    ===========
    offset=26 -> offset=0
"""
