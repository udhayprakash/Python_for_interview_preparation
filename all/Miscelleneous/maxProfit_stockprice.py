# def myfunc(stockPrices):
#     result = {}
#     for i in range(len(stockPrices)):
#         print(stockPrices[i], stockPrices[i+1:])


# print(myfunc([5, 4, 23, 2,  3, 5, 8, 9]))


# trades = [5, 4, 7, 2,  3, 5, 8, 9]

# minVal, minPos = trades[0], 0
# for index, trade in enumerate(trades):  # O(n)
# 	if trade < minVal:
# 		minVal = trade
# 		minPos = index

# maxVal= minVal
# for index, trade in enuemrate(trades):
# 	if index < minPos: continue
# 	if trade > maxVal:
# 		maxVal = trade


def maxProfit(k, profit):
    n = len(profit)
    pSum = [0] * (2 * n + 1)
    for i in range(n):
        pSum[i + 1] = pSum[i] + profit[i]
    for i in range(n):
        pSum[i + n + 1] = pSum[i + n] + profit[i]
    result = -1 * pow(2, 64)
    while i <= n // 2:
        csum = pSum[i + k] + pSum[i + n // 2 + k] - pSum[i] - pSum[i + n // 2]
        result = max(result, csum)
        i += 1
    return result


print(maxProfit(2, [1, 5, 1, 3, 7, 3]))
