"""
Purpose: Merge the tuples if their first element is common
"""


def myfunc(mylist):
    res = {}
    for tup in mylist:
        if tup[0] in res:
            res[tup[0]] = res[tup[0]] + tup[1:]
        else:
            res[tup[0]] = tup
    return res.values()


lt = [(1, 2), (1, 3), (1, 4), (2, 5), (3, 6)]
ot = [(1, 2, 3, 4), (2, 5), (3, 6)]
print(myfunc(lt))
