# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 计算斐波那契数列.py
# @Time       ：2023/8/17 19:25
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
计算斐波那契数列。具体什么是斐波那契数列，
那就是0，1，1，2，3，5，8，13，21，34，55，89，144，233。
"""
# ================【功能：】====================
def num_sushu(num):
    res = [0, 1, 1]
    sum = 2
    while sum < num:
        res.append(sum)
        sum = res[-2] + res[-1]
    return res


if __name__ == '__main__':
    num = 300
    res = num_sushu(num)
    print(res)