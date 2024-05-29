# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : func.py
# @Time       ：2023/8/15 8:51
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================

###############
# Book 4  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############


import sys

# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

n = 100
res = 0
for i in range(1, n + 1):
    temp = []
    for j in range(1, i):
        if i % j == 0:
            temp.append(j)
    if sum(temp) == i:
        res += 1
print(res)

# res = []
# for i in range(1, 28):
#     if 28 % i == 0:
#         res.append(i)
# if sum(res) == 28:
#     print('-----')
# print(res)
