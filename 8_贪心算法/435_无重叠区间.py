# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 435_无重叠区间.py
# @Time       ：2024/2/18 14:35
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================


def interval_schedule(intvs):
    if len(intvs) == 0:
        return 0

    # 排序
    intvs = sorted(intvs, key=lambda x: x[1], reverse=False)

    # 至少有一个
    num_count = 1
    # 排序后的x就是intvs中的第一个
    x_end = intvs[0][1]

    for intervals in intvs:
        x_start = intervals[0]
        if x_start >= x_end:
            num_count += 1
            x_end = intervals[1]
    return num_count



intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
res = interval_schedule(intervals)
print(res)





