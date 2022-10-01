class Solution:
    def isValid(self, s: str) -> bool:
        reversedNumber = 0
        if x > 0:
            while x > 0:
                reversedNumber = reversedNumber * 10 + x % 10
                x //= 10
                if reversedNumber >= 2**31 - 1 or reversedNumber <= -(2**31):
                    return 0
                else:
                    return reversedNumber
        elif x == 0:
            return 0
        elif x < 0:
            x = abs(x)
            while x > 0:
                reversedNumber = reversedNumber * 10 + x % 10
                x //= 10
                if reversedNumber >= 2**31 - 1 or reversedNumber <= -(2**31):
                    return 0
                else:
                    return -reversedNumber
