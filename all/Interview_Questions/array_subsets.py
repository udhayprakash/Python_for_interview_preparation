import copy


def subsetA(arr):
    print('\narr     :', arr)
    arr.sort()
    sub_arrA = []
    for index1, num1 in enumerate(arr):
        for index2, num2 in enumerate(arr):
            if index1 != index2:
                new_arr = copy.deepcopy(arr)
                try:
                    del new_arr[index1]
                    del new_arr[index2]
                except Exception as ex:
                    pass
                # print('\nnum1 + num2=', num1 + num2, 'sum(new_arr);', sum(new_arr))

                if (num1 + num2) >= sum(new_arr):
                    # print(num1 + num2, sum(new_arr), end='\t')
                    # print(num1, num2, '--->', new_arr)
                    if (sub_arrA
                            and sum(sub_arrA) < (num1 + num2)
                            or not sub_arrA):
                        sub_arrA = sorted((num1, num2))

    print('sub_arrA:', sub_arrA)
    return sub_arrA


if __name__ == '__main__':
    assert subsetA([3, 7, 5, 6, 2]) == [6, 7]  # [(5, 7), (6, 7)]
    assert subsetA([5, 3, 2, 4, 1, 2]) == [4, 5]
    assert subsetA([4, 2, 5, 1, 6]) == [5, 6]  # (5, 6), (4, 6)
    print(subsetA([2, 3, 4, 4, 5, 9, 7, 8, 6, 10, 4, 5, 10, 10, 8, 4, 6, 4, 10, 1]))
    [8, 8, 9, 10, 10, 10, 10]
