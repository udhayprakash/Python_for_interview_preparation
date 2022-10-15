import itertools


def permutations(arr):
    perm_arrs = set()
    for index, ele in enumerate(arr):
        rem_arr = arr[:index] + arr[index + 1 :]
        for i in range(len(arr)):
            new_arr = rem_arr.copy()
            new_arr.insert(i, ele)
            perm_arrs.add(tuple(new_arr))
    return perm_arrs


print(sorted(permutations([1, 2, 3])))
print(sorted(itertools.permutations([1, 2, 3])))


def permutations(given_list):
    if len(given_list) <= 1:
        yield given_list
        return
    for perm in permutations(given_list[1:]):
        for i in range(len(given_list)):
            # nb given_list[0:1] works in both string and list contexts
            yield perm[:i] + given_list[0:1] + perm[i:]


print(sorted(permutations([1, 2, 3])))


def permutations(a, k=0):
    if k == len(a):
        print(a)
    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i], a[k]
            permutations(a, k + 1)
            a[k], a[i] = a[i], a[k]


print(sorted(permutations([1, 2, 3])))
