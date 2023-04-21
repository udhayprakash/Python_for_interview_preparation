"""
Purpose: Custom Sort
    sorted characters in a string as
    lowercases first, uppercases next,  then evennumbers, and finally oddnumbers
"""
# def sort_func(x):
#     return (x.islower() , x.isupper(),
#             int(x)%2 == 0 if x.isnumeric() else False,
#             int(x)%2 != 0 if x.isnumeric() else False)


# def custum_sort(given_str):
#     result = sorted(given_str, key = lambda x: sort_func(x), reverse=True)
#     return "".join(result)

# assert custum_sort("SortingR132468")== "ortingSR246813"
# assert custum_sort("aAbBcCdDeEfF2461357") == "abcdefABCDEF2461357"


def custum_sort(string):
    lower_chars = []
    upper_chars = []
    even_nums = []
    odd_nums = []

    # Iterate through each character in the string
    for char in string:
        if char.islower():
            lower_chars.append(char)  # Add lowercase characters to lower_chars list
        elif char.isupper():
            upper_chars.append(char)  # Add uppercase characters to upper_chars list
        elif char.isdigit():
            if int(char) % 2 == 0:
                even_nums.append(char)  # Add even numbers to even_nums list
            else:
                odd_nums.append(char)  # Add odd numbers to odd_nums list

    # Sort the lists
    lower_chars.sort()
    upper_chars.sort()
    even_nums.sort()
    odd_nums.sort()

    # Combine the sorted lists into a single string
    sorted_string = "".join(lower_chars + upper_chars + even_nums + odd_nums)

    return sorted_string


print(custum_sort("SortingR132468") == "ginortRS246813")
