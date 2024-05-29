# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 9_基于分治策略和随机选择策略的快速排序.py
# @Time       ：2024/1/6 17:35
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
import random
def partition(arr, p, r):
    temp = p
    base = arr[p]
    mark = p
    while p <= r:
        if arr[p] < base:
            mark += 1
            arr[mark], arr[p] = arr[p], arr[mark]
        p += 1
    arr[temp], arr[mark] = arr[mark], arr[temp]
    return mark

def random_partition(arr, p, r):
    i = random.randint(p, r)
    arr[i], arr[p] = arr[p], arr[i]
    return partition(arr, p, r)

def quick_sort(arr, p, r):
    if p < r:
        q = random_partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)


arr = [4, 2, 8, 5, 7, 1, 3, 9, 6]
quick_sort(arr, 0, len(arr) - 1)
print(arr)






