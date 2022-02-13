def findSmallestDivisor(s,t):
    if(is_divisible(s, t)):
        return len(get_smallest_rep_str(t))
    else:
        return -1

def is_divisible(s, t):
    is_length_divisible = (len(s) % len(t)) == 0
    if(is_length_divisible):
        return t*(len(s)//len(t)) == s

def get_smallest_rep_str(string):
    for x in range(1, len(string)):
        sub_str = string[:x]

        if sub_str * (len(string)//len(sub_str)) == string:
            return sub_str
    return string

if __name__ == '__main__':
    assert findSmallestDivisor("lrbb", "lrbb") == 4
    assert findSmallestDivisor("lblb", "lblb") == 2