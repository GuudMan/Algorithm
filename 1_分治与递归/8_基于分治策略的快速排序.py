# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 8_基于分治策略的快速排序.py
# @Time       ：2024/1/6 15:56
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
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

def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)


arr = [4, 2, 8, 5, 7, 1, 3, 9, 6]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
