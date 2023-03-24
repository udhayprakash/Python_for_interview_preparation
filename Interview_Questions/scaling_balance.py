# def scaling_balance(arr):
#     w1, w2 = eval(arr[0])
#     available_weights = eval(arr[1])
#     weight_diff = abs(w1 - w2)
#     if weight_diff in available_weights:
#         return weight_diff

#     remaining_bal = []
#     for added_w1 in available_weights:
#         remaining_bal.append(added_w1 - )


# if __name__ == '__main__':
#     assert scaling_balance(['[3, 4]', '[1, 2, 7, 7]']) == 1
#     assert scaling_balance(['[13, 4]', '[1, 2, 3, 6, 14]']) == None


def scaling_balance(arr):
    left, right = eval(arr[0])
    weights = eval(arr[1])
    # Set a key to note original weight location [left or right]
    balance_key_init = 0 if left else 1

    init_weight = left + right
    print("Init weight: " + str(init_weight))

    for item in weights:
        # This takes care of any direct balancing matches
        if item == init_weight:
            if balance_key_init:
                left = left + item
            else:
                right = right + item
            return True

    # we get here because no direct weights match 5

    # ALGO:
    # Start by ordering the weights from smallest -> largest
    weights.sort()
    # > [1, 3, 4, 6]

    # Move from the smallest to largest an 'add them' to the next item
    # 1 + 3 = 4 != 5
    # 1 + 4 = 5 MATCH!!!
    # 1 + 6 = NO MATCH!
    for counter, item in enumerate(weights):
        for additionItem in weights[counter:]:
            if item + additionItem == init_weight:
                if balance_key_init:
                    left = left + (item + additionItem)
                else:
                    right = right + (item + additionItem)
                return True
        # IF MATCH, DONE
        # IF NO MATCH, MOVE ON TO NEXT NUMBER
        # 3 + 4 != 5
        # 3 + 6 != 5, etc

    # Solution is to have left - right == 0


print(scaling_balance(["[3, 4]", "[1, 2, 7, 7]"]))
