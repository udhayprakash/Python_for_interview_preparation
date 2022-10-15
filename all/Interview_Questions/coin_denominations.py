from audioop import reverse


def find_denominations(num, coins):
    denominations = {}
    if num <= 0 or not coins:
        return False, denominations
    coins.sort(reverse=True)

    for coin in coins:
        count = num // coin
        if count * coin == num:
            denominations[coin] = count
            break
        denominations[coin] = count - 1 if count else 0
        num -= coin * (count - 1) if count else 0

    total_value = sum(coin * count for coin, count in denominations.items())
    return total_value == num, denominations


for i in range(15):
    print(i, find_denominations(i, [10, 5, 2]))
