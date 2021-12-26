#!/usr/bin/python3
"""
Purpose: For the given array, perform digit level addition"""

def myfunc(arr, num):
    if not arr: return arr 
    i, arrLen, value = 0, len(arr), 0
    while i < arrLen:
        value += arr[arrLen - i -1] * (10 ** i)
        i += 1
    
    value += num 
    result = []
    while value:
        result.insert(0, value % 10)
        value //= 10 
    return result

if __name__ == '__main__':
    assert myfunc([1, 2, 3], 1) == [1, 2, 4]
    assert myfunc([1, 2], 1) == [1, 3]
    assert myfunc([1], 1) == [2]
    assert myfunc([], 1) == []
    assert myfunc([9], 1) == [1, 0]
