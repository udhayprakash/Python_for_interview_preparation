import re


def Wildcards(strParam):
    # print(f'\n\n\n{strParam=}\n')
    pattern, word = strParam.split()

    i = 0
    w = 0
    while i < len(pattern):  # and w <len(word):
        # print(f'{pattern[i] =}  {word[w] =}')
        if pattern[i] == "+":
            if word[w].isalpha():
                w += 1
                i += 1
                continue
            return False
        elif pattern[i] == "$":
            if word[w].isnumeric():
                w += 1
                i += 1
                continue
            return False
        elif pattern[i] == "*":
            if i + 1 < len(word) and pattern[i + 1] == "{":
                rep_count = int(pattern[i + 2])

            if word[w] == word[w + 1] == word[w + 2]:
                w += 3
                i += 1
                continue
            return False

        # if pattern[i] == '+' and word[w].isalpha():
        #   w += 1; i += 1
        # elif pattern[i] == '*' and (word[w] == word[w+1] == word[w+2]):
        #   w += 1; i += 1

        # i+= 1; w += 1
        return False

    return True


# keep this function call here
# print(Wildcards(input()))

print('Wildcards("++ ab")                :', Wildcards("++ ab"))
print('Wildcards("++++++++ qwertyuu")    :', Wildcards("++++++++ qwertyuu"))
print('Wildcards("$ 3")                  :', Wildcards("$ 3"))
print('Wildcards("$$$ 345")              :', Wildcards("$$$ 345"))

print('Wildcards("$++ 3bc")              :', Wildcards("$++ 3bc"))
print('Wildcards("$+$ 3b7")              :', Wildcards("$+$ 3b7"))

print('Wildcards("$+* 3b777")            :', Wildcards("$+* 3b777"))
print('Wildcards("** mmm777")            :', Wildcards("** mmm777"))

print('Wildcards("*{3} mmm")             :', Wildcards("*{3} mmm"))

# print('Wildcards("+++++* abcdehhhhhh"):', Wildcards("+++++* abcdehhhhhh"))
# print('Wildcards("++* abhhh")         :', Wildcards("++* abhhh"))

# print(Wildcards("$**+*{2} 9mmmrrrkbb") ==True)
#  $ * * + * { 2 }
#  $ + + + + + + + + +
#  0 1 2 3 4 5 6 7
#  9 mmm rrr k bb
#  $ + + + + + + + + +
#  9 m m m r r r k b b
# print(Wildcards("+++++* abcdehhhhhh")==False)
# print(Wildcards("++*{5} jtggggg")==True)


# ++*{5}
# jtggggg
# ++*****
