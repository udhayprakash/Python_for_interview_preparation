def solution(prices):
    if not prices:
        return 0
    elif len(prices) == 1:
        return prices[0]
    max_profit = 0
    for index, price in enumerate(prices):
        relative_gain = price - prices[index - 1]
        if relative_gain > max_profit:
            max_profit = relative_gain
    return max_profit


assert solution([6, 0, -1, 10]) == 11
assert solution([13, 10, 8, 4, 10]) == 6
print(
    solution(
        [
            338,
            -158,
            -329,
            186,
            -497,
            -362,
            410,
            -442,
            137,
            -180,
            222,
            270,
            160,
            51,
            212,
            54,
            185,
            -209,
            389,
            -381,
            107,
            -225,
            47,
            -232,
            -27,
            285,
            237,
            -258,
            479,
            -229,
            210,
            341,
            173,
            -471,
            -213,
            140,
            99,
            431,
            33,
            9,
            431,
            -431,
            -460,
            -182,
            24,
            -153,
            -253,
        ]
    )
)
