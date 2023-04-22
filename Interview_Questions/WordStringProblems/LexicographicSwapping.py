"""
Strings: Lexicographic Swapping
You are given two strings S and B, both of equal lengths. String S contains English letters ([a-z]), and string B contains a binary string having is and Os.
Find the lexicographically smallest string by swapping the characters in the position where there is "1" in the binary string.
Note: You can swap the characters any number of times.

Lexicographic order is the way of the ordering of words based on the alphabetical order of English letters, i.e. 'a' is the smallest letter and 'z' is the greatest letter.

S= "bcbxe" and B= "10011".

# OUTPUT [uncomment & modify if required] print(lexicographicallySmallest (N, S, B))
Here, positions 0, 3, and 4 are swappable. The characters in these positions are b, x, e. We will swap x and e and get the string "bcbex" which is the lexicographically smallest string possible.
Function Description
In the provided code snippet, implement the provided lexicographicallySmallest (...) method using the variables to find the lexicographically smallest string with the allowed operation. You can write your code in the space below the phrase "WRITE YOUR LOGIC HERE".
There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.
Output Test against custom input
"""


def lexicographicallySmallest(S, B):
    chars = [ch for ch, val in zip(S, B) if val == "1"]
    chars.sort()
    result = list(S)
    for index, ch in enumerate(S):
        if B[index] == "1":
            result[index] = chars.pop(0)
    return "".join(result)


lexicographicallySmallest(S="bcbxe", B="10011")

# Test case 1: Binary string has all zeros
assert lexicographicallySmallest("bcbxe", "00000") == "bcbxe"

# Test case 2: Binary string has all ones
assert lexicographicallySmallest("bcbxe", "11111") == "bbcex"

# Test case 3: Binary string has alternating zeros and ones
assert lexicographicallySmallest("bcbxe", "10101") == "bcbxe"

# Test case 4: Binary string has all zeros except the first position
assert lexicographicallySmallest("bcbxe", "10000") == "bcbxe"

# Test case 5: Binary string has all zeros except the last position
assert lexicographicallySmallest("bcbxe", "00001") == "bcbxe"

# Test case 6: Binary string has all ones except the first position
assert lexicographicallySmallest("bcbxe", "11110") == "bbcxe"

# Test case 7: Binary string has all ones except the last position
assert lexicographicallySmallest("bcbxe", "01111") == "bbcex"

# Test case 8: Binary string has only one "1" at the middle position
assert lexicographicallySmallest("bcbxe", "00100") == "bcbxe"

# Test case 9: Binary string has only one "1" at the first position
assert lexicographicallySmallest("bcbxe", "10000") == "bcbxe"

# Test case 10: Binary string has only one "1" at the last position
assert lexicographicallySmallest("bcbxe", "00001") == "bcbxe"
