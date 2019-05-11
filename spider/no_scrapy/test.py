#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: kris_peng
# Created on 2019/3/8

# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     dict = {}
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         dict[values[0]] = values[1]
#     left_dict = {}
#     right_dict = {}
#     left_list = []
#     right_list = []
#     for key in dict:
#         if key < 0:
#             left_dict[key] = dict[key]
#             left_list.append(key)
#         else:
#             right_dict[key] = dict[key]
#             right_list.append(key)
#
#     left_list.sort()
#     right_list.sort()
#
#     flag = ''
#     count = 0
#     if len(left_list) < len(right_list):
#         count = len(left_list)
#         flag = "right"
#     elif len(left_list) == len(right_list):
#         count = len(left_list)
#         flag = "no"
#     else:
#         count = len(right_list)
#         flag = "left"
#     ans_left = 0
#     ans_right = 0
#
#     if len(left_list) == 0:
#         ans = right_dict[right_list[0]]
#     elif len(right_list) == 0:
#         ans = left_dict[left_list[i]]
#     else:
#         i = 0
#         while i < count:
#             ans_left = ans_left + left_dict[left_list[-i]]
#             ans_left = ans_left + right_dict[right_list[i]]
#             i = i + 1
#         if flag == "left":
#             ans_left = ans_left + left_dict[left_list[-i]]
#
#         i = 0
#         while i < count:
#             ans_right = ans_right + right_dict[right_list[i]]
#             ans_right = ans_right + left_dict[left_list[-i]]
#             i = i + 1
#         if flag == "right":
#             ans_right = ans_right + right_dict[right_list[i]]
#         if ans_left > ans_right:
#             ans = ans_left
#         else:
#             ans = ans_right
#     print(ans)


# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = []
#     dict = {}
#     for i in range(3):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         dict[i+1] = [values[0], values[1]]
#     remain = n - dict[1][0] - dict[2][0] - dict[3][0]
#     if remain < dict[1][1] - dict[1][0]:
#         ans = str((n-dict[2][0] - dict[3][0])) + " " + str(dict[2][0]) + " " + str(dict[3][0])
#     elif remain < dict[2][1] - dict[2][0] + dict[1][1] - dict[1][0]:
#         ans = str(dict[1][1]) + " " + str(n - dict[3][0] - dict[1][1]) + " " + str(dict[3][0])
#     else:
#         ans = str(dict[1][1]) + " " + str(dict[2][1]) + " " + str(n - dict[2][1] - dict[1][1])
#     print(ans)

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

def square_numbers(nums):
    for i in nums:
        yield(i * i)

my_nums = square_numbers([1,2,3,4,5])
for num in my_nums:
    print(num)
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
