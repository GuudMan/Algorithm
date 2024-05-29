# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 70_爬楼梯.py
# @Time       ：2023/12/14 19:15
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
示例 1：
输入：n = 2
输出：2

解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
"""
# ================【功能：】====================
class Solution:
    memo = []
    def climbStairs(self, n: int) -> int:
        self.memo = [0] * (n + 1)
        return self.dp(n)

    def dp(self, n):
        if n <= 2:
            return n
        if self.memo[n] > 0:
            return self.memo[n]

        # 状态转移方程
        self.memo[n] = self.dp(n - 1) + self.dp(n - 2)
        return self.memo[n]




s = Solution()
res = s.climbStairs(2)
print(res)