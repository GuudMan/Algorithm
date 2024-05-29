# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 走方格.py
# @Time       ：2024/2/2 14:38
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""


# ================【功能：】====================
def fg(m, n):
    if m <= 0 or n <= 0:
        return 0
    elif m == 1 or n == 1:
        return 1
    else:
        return fg(m - 1, n) + fg(m, n - 1)


res = fg(3, 3)
print(res)
