"""
Problem: Get longest substring length
"""


def longest_substr_len(my_string: str) -> bool:
    longest_unique_substr = ""
    lus_len = 0
    for index, _ in enumerate(my_string):
        for sub_str in (my_string[index:], my_string[:index]):
            sub_str_len = len(sub_str)
            if sub_str_len == len(set(sub_str)) and lus_len < sub_str_len:
                longest_unique_substr = sub_str
                lus_len = len(longest_unique_substr)
    print(f"{my_string =}\t{longest_unique_substr =}")
    return len(longest_unique_substr)


def longest_substr_len(my_string: str) -> bool:
    # Creating a set to store the last positions of occurrence
    seen = {}
    maximum_length = 0

    # starting the inital point of window to index 0
    start = 0

    for end in range(len(my_string)):
        # Checking if we have already seen the element or not
        if my_string[end] in seen:
            # If we have seen the number, move the start pointer
            # to position after the last occurrence
            start = max(start, seen[my_string[end]] + 1)

        # Updating the last seen value of the character
        seen[my_string[end]] = end
        maximum_length = max(maximum_length, end - start + 1)
    return maximum_length


if __name__ == "__main__":
    assert longest_substr_len("abcdef") == 6
    assert longest_substr_len("bob") == 2
    assert longest_substr_len("apple") == 3
    assert longest_substr_len("beaba") == 3
    assert longest_substr_len("abcba") == 3
