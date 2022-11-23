def solution(prices):
    m = 0
    for i in range(0, len(prices)):
        for j in range(i + 1, len(prices)):
            m = max(m, prices[j] - prices[i])
    return m


def solution(prices):
    buy, m = 0, 0
    for i in range(len(prices)):
        buy = min(buy, prices[i])
        profit = prices[i] - buy
        m = max(m, profit)
    return m


def solution(prices):
    m = 0
    for i in range(0, len(prices) - 1):
        buy, sell = prices[i], max(prices[i + 1 :])
        m = max(m, sell - buy)
    return m


def solution(prices):
    max_profit = 0
    min_stock = float("inf")
    for price in prices:
        max_profit = max(max_profit, price - min_stock)
        min_stock = min(min_stock, price)
    return max_profit


assert solution([6, 0, -1, 10]) == 11
assert solution([13, 10, 8, 4, 10]) == 6
assert solution([10, 12, 9, 6, 8, 12]) == 6
assert solution([455, 460, 465, 451, 414, 415, 441]) == 27
assert solution([1, 5, 1, 3, 7, 3]) == 6
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
