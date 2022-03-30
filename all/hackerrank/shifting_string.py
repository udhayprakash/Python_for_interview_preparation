from functools import wraps
from time import process_time_ns


def time_taken(func):
    # @wraps()
    def inner(*args, **kwargs):
        start = process_time_ns()
        result = func(*args, **kwargs)
        print(f'TIME TAKEN:{process_time_ns() - start}')
        return result
    return inner


@time_taken
def getShiftedString(s, leftShifts, rightShifts):
    print("leftshift", leftShifts, "rightShifts", rightShifts)
    str_len = len(s)
    if leftShifts > str_len:
        leftShifts = leftShifts % str_len
    if rightShifts > str_len:
        rightShifts = rightShifts % str_len

        #print("original = ", s)
    for _ in range(leftShifts):
        s = s[1:] + s[0]
    #print('leftshift =', s)
    for _ in range(rightShifts):
        s = s[-1] + s[:-1]
    #print("rightshift =", s)
    return s


if __name__ == '__main__':
    assert getShiftedString("abcdef", 10, 8) == "cdefab"
    assert getShiftedString("abcdef", 4, 8) == "cdefab"
