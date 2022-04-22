def check_relations(listOfPairs):
    """
    if match found, it will merge matched tuples;
    if not match, it will return input listOfPairs
    :input listOfPairs: list of tuples
    :output: list of tuples
    """
    # sorting based on start position number, in each tuple
    listOfPairs.sort(key=lambda x: x[0])
    print("listOfPairs", listOfPairs)

    result = []
    del_indices = []
    for index, curPair in enumerate(listOfPairs):
        if index == 0:
            continue  # skipping first loop for comparision

        prePair = listOfPairs[index - 1]
        if curPair[0] - prePair[1] < 0:
            listOfPairs[index] = (
                min([curPair[0], prePair[0]]),
                max([curPair[1], prePair[1]]),
            )
            del_indices.append(index)
            result.append(
                (min([curPair[0], prePair[0]]), max([curPair[1], prePair[1]]))
            )
    print("listOfPairs", listOfPairs, "ind", del_indices, len(listOfPairs))
    for d_indx in del_indices[::-1]:
        del listOfPairs[d_indx]
    print("after del, listOfPairs", listOfPairs)
    return result if result else listOfPairs


# assert check_relations([(7,9), (1, 3), (6, 8), (2, 5)]) == [(1, 5), (6, 9)]
# assert check_relations([(4,7), (3,5)]) == [(3, 7)]
# assert check_relations([(1, 3), (4, 5)]) ==[(1, 3), (4, 5)]

print(check_relations([(1, 3), (4, 5), (2, 7)]))
# assert check_relations([(1, 3), (4, 5), (2, 7)]) ==[(1, 7)]
