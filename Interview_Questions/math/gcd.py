import math


def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


assert gcd(50, 40) == math.gcd(50, 40)
