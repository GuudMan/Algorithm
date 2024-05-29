# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 股票交易.py
# @Time       ：2024/2/18 15:21
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================

# dp[i][k][0 or 1]
# 0 <= i <= n - 1, 1 <= k <= K
# n为天数， k为最多交易数
# 此问题一共有n × K × 2种状态， 全部枚举就能全部搞定
n = 4
K = 2
dp = [[[0] * n for _ in range(K)] for _ in range(2)]
for i in range(n):
    for k in range(1, K):
        for s in [0, 1]:
            dp[i][k][s] = max(buy, sell, rest)








