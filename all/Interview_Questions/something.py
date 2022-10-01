def test(x):
    if x % 3 == 0:
        return test(x / 3)
    if x % 2 == 1:
        return x
    return test(2 * x + 1)


print(test(100))

# class A(object):
#     def __init__(self):
#         print('A')
#         super(A, self).__init__()
#         print('<A>')


# class B(object):
#     def __init__(self):
#         print('B')
#         super(B, self).__init__()
#         print('<B>')


# class C(A, B):
#     def __init__(self):
#         print('C')
#         super(C, self).__init__()
#         print('<C>')


# C()


# from string import *
# method = "METHODS"


# def x(methods):
#     method = str.swapcase(methods)
#     print(("%(method)s" % locals()))


# methods = str.swapcase(method[:-1])
# x(methods)


# n = 12
# names = [[]] * n

# employee = 'Adam'
# m = 6
# names[m].append(employee)
# print(names)


# x = 1
# y = 0
# z = 0
# result = 2
# try:
#     z = z + 1
#     result = x / y
#     z = z + 1
# except ZeroDivisionError:
#     z = z + result
# else:
#     z = z + 1
# finally:
#     z = z + 1
# z = z + 1
# print(z)


# z = 5
# x = '456'
# while z > -1:
#     y = x
#     if y in ('1', '2', '3') or len(y) > 1:
#         break
#     x = x + y
#     if y in ('4', '5', '6'):
#         continue
#     z = z - 1
# print(z)


# class subject():
#     count = 0

#     def __init__(self, name):
#         self.name = name

#     def set(self, name):
#         self._name = name

#     def get(self):
#         return self._name

#     name = property(get, set)


# s = subject('udhay')


# import random
# string = 'avsdbc'
# n = 3

# password = "".join(random.sample(string, n))
# print(password)

# password = ''.join(random.choice(string) for _ in range(n))
# print(password)

# password = ''.join(random.choice(string) * 3)
# print(password)

# string = random.choice(string)
# lst = [string for x in range(n)]
# password = ''.join(lst)
# print(password)

# lst = list(string)
# random.shuffle(lst)
# password = ''.join(lst[:n])
# print(password)


# def sq(x):
#     return x * x


# def recursive_map(func, seq):
#     if seq == []:
#         return seq
#     else:
#         return [func(seq[0])] + recursive_map(func, seq[1:])


# print(recursive_map(sq, [1, 2, 3]))


# def recursive_map(func, seq):
#     if seq == []:
#         return seq
#     else:
#         return recursive_map(func, seq[1:]) + [func(seq[0])]


# print(recursive_map(sq, [1, 2, 3]))
