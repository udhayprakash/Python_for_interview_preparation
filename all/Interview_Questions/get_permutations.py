import itertools


def permutations(listOfChars):
    result = []
    for each in itertools.permutations(listOfChars):
        result.append(''.join(each))
    return result


def permutations(listOfChars):
    if len(listOfChars) <= 1:
        yield listOfChars
    else:
        for each in permutations(listOfChars[1:]):
            for i in range(len(listOfChars)):
                comb = list(each[:i]) + listOfChars[0:1] + list(each[i:])
                yield ''.join(comb)


print(list(permutations(['a', 'b', 'c'])))
print(list(permutations(['a', 'b', 'c', 'd'])))
