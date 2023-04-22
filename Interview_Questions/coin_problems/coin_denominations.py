"""
Problem:
    your input is representing coins of different denominations and an integer
    amount representing a total amount of money.
    Return the fewest number of coins that you need to make up that amount.
    If that amount of money cannot be made up by any combination of the coins,
    return -1.

    Input: c = [1,2,5], amount = 11
    Output: 3
"""


def find_denominations(denominations, amount):
    denominations.sort(reverse=True)
    cts = {}
    for coin in denominations:
        coin_ct = amount // coin
        amount -= coin_ct * coin
        if coin_ct:
            cts[f"{coin}Dollars"] = coin_ct
    return -1 if amount else cts


if __name__ == "__main__":
    print(find_denominations([1, 2, 5], 11))
    print(find_denominations([11, 9, 7, 5, 1], 25))

    for i in range(15):
        print(i, find_denominations([10, 5, 2], i))
