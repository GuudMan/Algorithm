# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 4_二分搜索.py
# @Time       ：2024/1/4 18:59
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================


def binary_search(num_list, x):
    num_list.sort()
    # 找到x就返回x在num_list中的位置，否则返回-1
    left = 0
    right = len(num_list) - 1
    while left <= right:
        middle = int((left + right) / 2)
        if x == num_list[middle]:
            return middle
        if x > num_list[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return -1


res = binary_search([2, 4, 1, 5, 6, 0, 12, 3, 2], 0)
print(res)




















