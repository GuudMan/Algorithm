# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 找零钱问题.py
# @Time       ：2024/1/25 10:34
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
def change(n, coins):
    c_n = len(coins)
    dp = [[0] * (n + 1) for _ in range(c_n)]
    for i in range(1, c_n):
        for j in range(1, n):
            if j - coins[i - 1] >= 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
    return dp[c_n][n]




amount = 5
coins = [1, 2, 4]
res = change(5, coins)
print(res)