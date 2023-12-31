"""
#164
Google

You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}.
By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.

"""
import secrets


def generateList():
    n = secrets.SystemRandom().randint(10, 100)
    l = [x for x in range(1, n)]
    l.append(secrets.SystemRandom().choice(l))
    secrets.SystemRandom().shuffle(l)
    return l


def summationTillN(n):
    return int(n * (n + 1) / 2)


def findDuplicate(l):
    actualSum = sum(l)
    expectedSum = summationTillN(len(l) - 1)
    return actualSum - expectedSum


def findDuplicateUsingCount(l):
    return [x for x in l if l.count(x) == 2][0]


def main():
    testCaseCount = 10
    testCasesPassed = 0
    testCasesFailed = 0

    for _ in range(testCaseCount):
        listWithDuplicate = generateList()
        duplicateValue = findDuplicate(listWithDuplicate)
        duplicateValueUsingCount = findDuplicateUsingCount(listWithDuplicate)
        try:
            assert duplicateValue == duplicateValueUsingCount
            print(listWithDuplicate, duplicateValue)
            testCasesPassed += 1
        except Exception:
            print("Error:", listWithDuplicate, duplicateValue, duplicateValueUsingCount)
            testCasesFailed += 1

    print()
    print("Total test cases:", testCaseCount)
    print("Test cases passed:", testCasesPassed)
    print("Test cases failed:", testCasesFailed)


if __name__ == "__main__":
    main()
