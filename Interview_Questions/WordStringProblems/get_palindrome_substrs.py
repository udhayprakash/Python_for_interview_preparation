import enum


def get_palindrome_substrs(givenStr):
    unique_palindrome_substrs = set()
    if givenStr == givenStr[::-1]:
        unique_palindrome_substrs.add(givenStr)
    for i, _ in enumerate(givenStr):
        j = 0
        while j < len(givenStr):
            substr = givenStr[j : j + i]
            if substr == substr[::-1]:
                unique_palindrome_substrs.add(substr)
            j += 1

    return unique_palindrome_substrs


print(get_palindrome_substrs("adada"))
assert get_palindrome_substrs("adada") == {"", "ada", "a", "d", "adada", "dad"}
