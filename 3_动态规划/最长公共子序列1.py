# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 最长公共子序列1.py
# @Time       ：2024/1/26 10:56
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""


# ================【功能：】====================
def lcs(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    # dp = [[0] * (l1 + 1) for _ in range(l2 + 1)]
    dp = [[0 for i in range(l1 + 1)] for j in range(l2 + 1)]
    for i in range(1, l2 + 1):
        for j in range(1, l1 + 1):
            if s2[i - 1] == s1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


res = lcs("abcde", "ace")
print(res)






