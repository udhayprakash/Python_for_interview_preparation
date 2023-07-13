#!/usr/bin/python
"""
Purpose: Binary to Decimal

    Input :  binary = "101"
    Output :   5

    Input :  binary = "1111"
    Output :   15

8 4 2 1
1 1 1 1 = 1*8 + 1*4 + 1*2 + 1*1 = 15


bits    - 0 & 1
1 byte  - 8 bits
        - 2 nibbles
1 nibble - 4 bits

    128 64 32 16 8 4 2 1
7     0  0  0  0 0 1 1 1
11    0  0  0  0 1 0 1 1
13    0  0  0  0 1 1 0 1
17    0  0  0  1 0 0 0 1
19    0  0  0  1 0 0 1 1
59    0  0  1  1 1 0 1 1
"""
# for i in range(11):
#     print(f'{i:2} {2 ** i:7} {bin(2 ** i)}')

# # decimal to binary -> bin(decimal) => binary

# Method 0 - using built-in - int()
print(f'\n{int("00000111", base=2) =}')
print(f'{int("00001011", base=2) =}')
print(f'{int("00001101", base=2) =}')
print(f'{int("00010001", base=2) =}')
print(f'{int("00010011", base=2) =}')
print(f'{int("00111011", base=2) =}')
print()

# Method 1 - using Iterations


def binary2decimal(binary_num):
    binary_num = binary_num.lstrip("0")
    result = 0
    for _index, bit in enumerate(binary_num[::-1]):
        # print(f'{(2 ** _index) =} {int(bit) =}')
        result += (2**_index) * int(bit)

    return result


assert binary2decimal("00000111") == 7
assert binary2decimal("111") == 7

print(f"{binary2decimal('00001011') =}")


# Method 2 - using iterations
def binary2decimal_2(binary_num: str):
    print()
    binary_num = binary_num.lstrip("0")

    result = 0
    counter = len(binary_num) - 1
    for each_digit in binary_num:
        # print(f'{2 ** counter =}, {each_digit =}, {result =}')
        result += (2**counter) * int(each_digit)
        counter -= 1
    return result


assert binary2decimal_2("00000111") == 7
assert binary2decimal_2("1011") == 11
assert binary2decimal_2("00001011") == 11
assert binary2decimal_2("00001101") == 13
assert binary2decimal_2("00010001") == 17
assert binary2decimal_2("00010011") == 19
assert binary2decimal_2("00111011") == 59
