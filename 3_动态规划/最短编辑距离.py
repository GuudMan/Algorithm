# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 最短编辑距离.py
# @Time       ：2024/1/26 9:28
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""


# ================【功能：】====================

def min_distance(r, d):
    m = len(r)
    n = len(d)
    dp = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = i
    for i in range(1, m + 1):
        dp[0][i] = i
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if d[i - 1] == r[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  # 插入
                    dp[i][j - 1] + 1,  # 删除
                    dp[i - 1][j - 1] + 1  # 替换
                )
    return dp[n][m]


res = min_distance("horse", "ros")
print(res)
