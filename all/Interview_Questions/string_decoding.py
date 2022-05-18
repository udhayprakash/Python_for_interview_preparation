"""
Purpose: String Decoding 

we have an input string 'id', which is formatted as follows:
x{value} -- where the string value inside the curly braces is repeated x number times.
x is always a positive integer, x > 1,
value consists of alphabet characters
All open curly braces have matching closed braces.

For example, these strings would translate as follows:

b2{o}2{k}2{e}per => bookkeeper
2{ra}2{dz} => raradzdz
5{a}2{b} => aaaaabb
10{a} => aaaaaaaaaa
a2bc3{d} => a2bcddd
"""
def decodeContainerId(input):
    resStr, repWord, num = '', '', 0
    for index, eachChar in enumerate(input):
        if eachChar == '{':
            numstr = ''
            j = index - 1
            while j >= 0:
                if not input[j].isdigit():
                    break
                numstr = input[j] + numstr 
                j -= 1
            if not numstr: continue
            resStr = resStr[:-len(numstr)]
            num = int(numstr)
        elif eachChar == '}':
            resStr += num * repWord
            repWord, num = '', 0
        else:
            if num:
                repWord += eachChar
            else:
                resStr += eachChar
    return resStr


assert decodeContainerId('b2{o}2{k}2{e}per') == 'bookkeeper'
assert decodeContainerId('2{ra}2{dz}') == 'raradzdz'
assert decodeContainerId('5{a}2{b}') == 'aaaaabb'
assert decodeContainerId('10{a}') == 'aaaaaaaaaa'
assert decodeContainerId('a2bc3{d}') == 'a2bcddd'