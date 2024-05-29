# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 整数划分.py
# @Time       ：2024/1/2 19:52
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================

def num_sub(n, m):
    if n < 1 or m < 1:
        return 0
    if n == 1 or m == 1:
        return 1
    if n < m:
        return num_sub(n, n)
    if n == m:
        return num_sub(n, m - 1) + 1
    return num_sub(n, m - 1) + num_sub(n - m, m)


def num_div(num):
    res = 0
    # for i in range(1, num):
    res += num_sub(num, num)
    return res
res = num_div(6)
print(res)