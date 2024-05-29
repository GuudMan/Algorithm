# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 7_自然合并排序.py
# @Time       ：2024/1/6 15:08
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
def find_sorted_subsequences(arr):
    subsequences = []
    start = 0
    end = 0
    n = len(arr)

    while end < n-1:
        # 找到下一个已排序的子序列
        while end < n-1 and arr[end] <= arr[end + 1]:
            end += 1

        subsequences.append(arr[start:end+1])
        start = end + 1
        end += 1

    return subsequences


def merge(sorted_subsequences):
    while len(sorted_subsequences) > 1:
        merged_subsequences = []
        i = 0
        while i < len(sorted_subsequences):
            if i+1 < len(sorted_subsequences):
                merged = sorted_subsequences[i] + sorted_subsequences[i+1]
                merged.sort()
                merged_subsequences.append(merged)
                i += 2
            else:
                merged_subsequences.append(sorted_subsequences[i])
                i += 1
        sorted_subsequences = merged_subsequences

    return sorted_subsequences[0]


def natural_merge_sort(arr):
    subsequences = find_sorted_subsequences(arr)
    sorted_arr = merge(subsequences)
    return sorted_arr


# 测试示例
arr = [1, 5, 2, 3, 6, 0, 7, 4, 8]
sorted_arr = natural_merge_sort(arr)
print(sorted_arr)

