def min_no_of_coins(num):
    print("\n========", num)
    coins = (11, 9, 7, 5, 1)
    count = 0
    for each_coin in coins:
        # if num % each_coin != num:
        quotient, remainder = divmod(num, each_coin)
        if quotient == 0:
            continue
        print(num, each_coin, divmod(num, each_coin))  # , end="\t===")
        num -= quotient * each_coin
        count += 1  # quotient if remainder == 0 else 1
        # num = remainder
        # print(num, each_coin)

    return count
