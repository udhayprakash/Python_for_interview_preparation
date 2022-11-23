# Strobogrammatic number
# Number is read the same if flipped 180 degrees
# 101 --> 101 (true)
# 6969 --> 6969 (true)
# 505 (false)


def strobogrammatic_check(number: int):
    flip_pairs = {"9": "6", "8": "8", "6": "9", "1": "1", "0": "0"}
    number = str(number)  # "101"
    i = len(number) - 1  # 2
    while i >= 0:
        if not (number[i] in flip_pairs.keys()):
            return False
        if number[len(number) - i - 1] != flip_pairs[number[i]]:
            return False
        i -= 1  # 0
    return True


assert strobogrammatic_check("101") is True
assert strobogrammatic_check("6969") is True
assert strobogrammatic_check("505") is False
