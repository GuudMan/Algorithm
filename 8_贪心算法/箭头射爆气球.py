# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 箭头射爆气球.py
# @Time       ：2024/2/18 14:59
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""


# ================【功能：】====================
def find_min_arrow_shots(intvs):
    if len(intvs) == 0:
        return 0
    intvs = sorted(intvs, key=lambda x: x[1], reverse=False)
    res_num = 1
    x_end = intvs[0][1]
    for interval in intvs:
        start = interval[0]
        if start > x_end:
            res_num += 1
            x_end = interval[1]

    return res_num


intervals = [[10, 16], [2, 8], [1, 6], [7, 12], [19, 29]]
res = find_min_arrow_shots(intervals)
print(res)
