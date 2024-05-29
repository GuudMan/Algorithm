# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 70_爬楼梯.py
# @Time       ：2024/1/16 19:55
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""
# ================【功能：】====================

class Solution(object):
    def climbStairs(self, n):
        self.memo = [0] * (n + 1)
        return self.dp(n)

    def dp(self, n):
        if n <= 2:
            return n
        if self.memo[n] > 0:
            return self.memo[n]
        # 爬到第 n 级台阶的方法个数等于爬到 n - 1 的方法个数和爬到 n - 2 的方法个数之和
        self.memo[n] = self.dp(n - 1) + self.dp(n - 2)
        return self.memo[n]

s = Solution()
res = s.climbStairs(3)
print(res)

