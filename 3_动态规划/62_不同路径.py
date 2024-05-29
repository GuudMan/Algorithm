# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 62_不同路径.py
# @Time       ：2024/1/16 20:11
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？
"""
# ================【功能：】====================
class Solution(object):
    def uniquePaths(self, m, n):
        self.memo = [[0] * (n + 1) for _ in range((m + 1))]
        return self.dp(m, n)

    def dp(self, m, n):
        if m == 1 and n == 1:
            return 1
        if m < 1 or n < 1:
            return 0
        if self.memo[m][n] > 0:
            return self.memo[m][n]
        self.memo[m][n] = self.dp(m - 1, n) + self.dp(m, n - 1)
        return self.memo[m][n]

s = Solution()
res = s.uniquePaths(7, 3)
print(res)
