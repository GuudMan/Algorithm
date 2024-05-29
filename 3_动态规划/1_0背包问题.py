# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 1_0背包问题.py
# @Time       ：2024/1/24 17:21
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
def package(n, w, wt, vt):
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if j - wt[i-1] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wt[i - 1]] + vt[i - 1])
    return dp[n][w]



n = 3
w = 4
wt = [2, 1, 3]
vt = [4, 2, 3]
res = package(n, w, wt, vt)
print(res)