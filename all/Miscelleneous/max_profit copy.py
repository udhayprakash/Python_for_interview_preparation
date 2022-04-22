def solution(prices):
    if not prices:
        return 0
    elif len(prices) == 1:
        return prices[0]
    profits = []
    for index, price in enumerate(prices):
        print(index, price)


print(solution([5, 2, 1, 6, 7, 9, 3]))
