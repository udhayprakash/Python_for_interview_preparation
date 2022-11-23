# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    # if len(S) == len(set(S)):
    #     # for all characters only occuring once
    #     return 1
    words = []
    currentSubstr = ""
    for eachChr in S:
        if eachChr in currentSubstr:
            words.append(currentSubstr)
            currentSubstr = eachChr
        else:
            currentSubstr += eachChr
    else:
        words.append(currentSubstr)
        print(eachChr, currentSubstr, words)
    print(words)
    return len(words)


assert solution("world") == 1  # ['world']
assert solution("dddd") == 4  # ['d','d', 'd','d']
assert solution("cycle") == 2  # ['cy', 'cle']
assert solution("abba") == 2  # ['ab', 'ba']
assert solution("abababa") == 4  # ['ab', 'ba']
