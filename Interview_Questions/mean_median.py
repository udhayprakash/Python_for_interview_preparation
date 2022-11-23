"""
Purpose:
	1. Define a function that returns the mean
	2. Define a function that returns the median
	https://www.investopedia.com/terms/m/median.asp

"""


def mean(givenList):
    return sum(givenList) / len(givenList)


def median(givenList):
    givenList.sort()
    if len(givenList) % 2:  # odd no. of values
        return givenList[len(givenList) // 2]
    else:
        midIndex = len(givenList) // 2
        return (givenList[midIndex] + givenList[midIndex - 1]) / 2


print(mean([2, 4, 6, 9, 10, 2]))
print(median([2, 4, 6, 9, 10, 2]))
print(median([2, 4, 6, 9, 10, 2, 7]))
