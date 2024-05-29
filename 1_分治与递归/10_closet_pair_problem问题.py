# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 10_closet_pair_problem问题.py
# @Time       ：2024/1/8 19:15
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
import math


def distance(p1, p2):
    """计算两个点的距离"""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


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


def quick_sort(r, first, end):
    if first < end:
        pivot = partition(r, first, end)
        quick_sort(r, first, pivot - 1)
        quick_sort(r, pivot + 1, end)


def closet(s, low, high):
    p = []
    if high - low == 1:
        return distance(s[low], s[high])

    # 如果有三个点， 求最近点对距离
    if high - low == 2:
        d1 = distance(s[low], s[low + 1])
        d2 = distance(s[low + 1], s[high])
        d3 = distance(s[low], s[high])
        return min(d1, d2, d3)

    mid = (low + high) // 2
    d1 = closet(s, low, mid)
    d2 = closet(s, mid + 1, high)

    d = min(d1, d2)

    # 建立点集p1
    for i in range(mid, low - 1, -1):
        if s[mid][0] - s[i][0] < d:
            p.append(s[i])

    # 建立点集p2
    for i in range(mid, high + 1):
        if s[i][0] - s[mid][0] < d:
            p.append(s[i])
    index = len(p)
    # 对p1, p2按y坐标升序排列
    quick_sort(p, 0, index - 1)

    # 处理p1和p2中的点
    for i in range(index):
        for j in range(i, index):
            if p[j][1] - p[i][0] >= d:
                break
            else:
                d3 = distance(p[i], p[j])
                d = min(d3, d)
    return d


if __name__ == '__main__':
    points = [(1, 2), (1, 20), (5, 6), (7, 8), (9, 10), (11, 12)]
    n = len(points)
    min_dist = closet(points, 0, n - 1)
    print(min_dist)





















