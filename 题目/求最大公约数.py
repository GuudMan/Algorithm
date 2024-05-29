# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 求最大公约数.py
# @Time       ：2023/8/15 19:28
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定两个自然数，求这两个数的最大公约数
"""
# ================【功能：】====================

def num(num1, num2):
    while num1 != num2:
        if num1 > num2:
            if num1 % num2 == 0:
                return num2
            num1 = num1 % num2
        else:
            if num2 % num1 == 0:
                return num1
            num2 = num2 % num1
    return num1


if __name__ == '__main__':
    num1 = 20
    num2 = 8
    res = num(num1, num2)
    print(res)
