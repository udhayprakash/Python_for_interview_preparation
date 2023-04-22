# IKM

# from string import *

# method = "METHODS"

# def x(methods):
#     method = str.swapcase(methods)
#     print("%(method)s" % locals())

# methods = str.swapcase(method[:-1])
# x(methods)


class I:
    num = 0

    def __init__(self) -> None:
        self.num = 0

    def method(self):
        return

    def methodA(self):
        I.num = 0

    def methodB(self):
        I.num += 1

    def methodC(self):
        self.num += 1

    def methodD(cls):
        I.num = I.num + 1

    methodD = classmethod(methodD)

    def methodE(cls):
        return I.num

    methodE = classmethod(methodE)

    def methodF():
        return I.num

    methodF = staticmethod(methodF)

    def methodG(self):
        self.num = self.num + 1

    def methodH(self):
        self.num = I.num
        return self.num


# print(f"{I.methodE() =}")

# K = I()

# print(f"{K.methodG() = }")
# print(f"{K.methodE() = }")

# # print(f'{I.methodB() =}')
# # print(f'{I.methodH() =}')
# print(f"{I.methodF() =}")

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             break
#     else:
#         print(n)
