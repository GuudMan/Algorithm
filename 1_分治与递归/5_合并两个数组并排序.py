# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 5_合并两个数组并排序.py
# @Time       ：2024/1/6 14:37
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""


# ================【功能：】====================

def merge(a, b):
    result = []
    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))

    result.extend(a)
    result.extend(b)
    return result


res = merge([1, 4, 5], [0, 2, 23])
print(res)
