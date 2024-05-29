# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 5_合并排序.py
# @Time       ：2024/1/4 19:26
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================

def merge(left, right):
    # 用于存放合并结果的列表
    result = []
    while len(left) > 0 and len(right) > 0:
        # 比较左右两个序列的首元素， 将较小的元素添加到列表中
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # 剩余元素添加到结果列表中
    result.extend(left)
    result.extend(right)
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2 # 找到序列的中间位置
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


arr = [6, 8, 1, 5, 9, 3, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)







