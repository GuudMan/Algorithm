# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 分治与递归_阶乘.py
# @Time       ：2024/1/2 19:23
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================

def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)

res = fact(4)
print(res)