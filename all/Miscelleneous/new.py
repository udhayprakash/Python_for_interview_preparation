# number = [1, 2, 2, 4, 4]

# # final_triplets = []
# # for index, _ in enumerate(arr):
# #     sub_arr = arr[index: index+3]
# #     if len(sub_arr) == 3:
# #         sub_arr.sort()
# #         del sub_arr[1]
# #         del sub_arr[-1]
# #         final_triplets.append(arr[:index] + sub_arr + arr[index+3:])
# # print(len(final_triplets))

# uniques = []
# dups = []
# for each in number:
#     if number.count(each) == 1:
#         uniques.append(each)
#     else:
#         dups.append(each)

# picked_triplets = []
# index = 0
# num_len = len(number)
# while index < num_len:
#     print('number', number)
#     for sub_index, each_num in enumerate(number):
#         sub_array = number[sub_index:sub_index+3]
#         if len(sub_array) == 3:
#             sub_array.sort()
#             print(number[:sub_index] + [sub_array[1]] + number[sub_index+3:])
#             number = number[:sub_index] + [sub_array[1]] + number[sub_index+3:]
#     index += 1


# def a():
#     if len(number) == 3:
#         number.sort()
#         return number[1]
#     else:


# assert a([1, 2, 2]) == [2]
# assert a([4, 4, 4]) == [4]
# assert a([1, 2, 2, 4, 4]) == [1, 2, 4]

# 1, 2, 2, 4, 4

# 1, 2, 2
#       2, 4, 4
#             4
