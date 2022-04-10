import random


def shuffle(givenlist):
    newlist = []
    for i in range(len(givenlist)):
        ele = random.choice(givenlist)
        givenlist.remove(ele)
        newlist.append(ele)
    return newlist


print(shuffle([1, 2, 3, 4, 5]))


def shuffle(givenlist):
    for i in range(len(givenlist)):
        ele = random.choice(givenlist[i:])
        eleIndex = givenlist.index(ele, i)
        givenlist[i], givenlist[eleIndex] = givenlist[eleIndex], givenlist[i]
    return givenlist


print(shuffle([1, 2, 3, 4, 5]))
