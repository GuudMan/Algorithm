# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 子集拆分.py
# @Time       ：2024/1/25 11:11
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
def change(ins):
    n = len(ins)
    ins_sum = sum(ins) // 2
    dp = [[False] * (ins_sum + 1) for _ in range(n + 1)]
    for i in range(1, n):
        for j in range(1, ins_sum):
            if j - ins[i - 1] >= 0:
                dp[i][j] = dp[i - 1][j] | dp[i - 1][j - ins[i - 1]]

    return dp[n][ins_sum]



ins = [1, 5, 11, 5]
res = change(ins)
print(res)