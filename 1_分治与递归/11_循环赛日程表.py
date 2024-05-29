# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 11_循环赛日程表.py
# @Time       ：2024/1/11 18:47
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
import numpy as np

def init(a, d):
    for i in range(d):
        a[0, i] = i + 1

def solveTable(n, a):
    Hf = int(len(a) / 2)
    if n == 1:
        a[0][0] = 1
        return
    temp = int(n / 2)
    solveTable(temp, a[0:Hf, 0:Hf])
    for i in range(Hf):
        for j in range(Hf):
            a[i, j + Hf] = a[i, j] + Hf
            a[i + Hf][j] = a[i][j + Hf]
            a[i + Hf][j + Hf] = a[i][j]


if __name__ == '__main__':
    k = 3
    d = 2 ** int(k)
    a = np.zeros((d, d))
    init(a, d)
    solveTable(d, a)
    print(a)



