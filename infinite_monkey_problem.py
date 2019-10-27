#!/usr/bin/python
"""
Purpose: 

https://en.wikipedia.org/wiki/Infinite_monkey_theorem
https://www.youtube.com/watch?v=Q6BBzmldu2w

https://www.youtube.com/watch?v=tOD6g7rF7NA

Sample Input:
    - 3141592653589793238462643383279
    - ['314', '49', '9001', '15926535897', '14', '9323', '8462643383279', '4', '793']

Sample Output:
    - 3(314 15926535897 9323 8462643383279)
      as three whitespaces are required to join them to make the original number
"""
import re

def spaces_required_to_make_number(given_no, favourite_nums):
    favourite_nums.sort(key= lambda x:len(x), reverse=True)

    result = []
    for ech_number in favourite_nums:
        if given_no:
            # print(len(given_no), given_no)
            m = re.search(ech_number, given_no)
            if m:
                # print(ech_number, m.span())
                result.append(ech_number)
                given_no = given_no[:m.start()] + given_no[m.end():]

    # print(result, len(result) -1)
    return len(result) -1

if __name__ == '__main__':
    assert spaces_required_to_make_number(
        '3141592653589793238462643383279',
        ['314', '49', '9001', '15926535897', '14', '9323', '8462643383279', '4', '793']
    ) == 3