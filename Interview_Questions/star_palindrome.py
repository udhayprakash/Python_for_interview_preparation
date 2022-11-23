import heapq


def star_palindrome(o_key: str) -> bool:
    keylen = len(o_key) // 2
    diffcount = 0
    for i in range(keylen - 1):
        if o_key[i] != o_key[keylen - i - 1]:
            diffcount += 1
            print(o_key, f"{diffcount =}")
            if diffcount >= 2:
                return False
    print(o_key, f"{diffcount =}")
    return True


"""
revive* <--> reviver
l**el <--> too obscured ignore -- despite middle * guarantees a valid palindrome
aa* <--> aaa (potential palindrome match)

"""
