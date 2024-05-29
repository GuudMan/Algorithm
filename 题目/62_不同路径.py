# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 62_不同路径.py
# @Time       ：2023/12/12 19:28
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？
输入：m = 3, n = 7
输出：28
示例 2：
输入：m = 3, n = 2

输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下

示例 3：
输入：m = 7, n = 3
输出：28

示例 4：
输入：m = 3, n = 3
输出：6
"""
# ================【功能：】====================
class Solution:
    memo = []
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = [[0] * n for _ in range(m)]
        return self.dp(m - 1, n - 1)

    # 定义: 从(0, 0)到(x, y)有dp(x, y)条路径
    def dp(self, x, y):
        if x == 0 and y == 0:
            return 1
        if x < 0 or y < 0:
            return 0
        if self.memo[x][y] > 0:
            return self.memo[x][y]
        self.memo[x][y] = self.dp(x - 1, y) + self.dp(x, y - 1)
        return self.memo[x][y]

s = Solution()
res = s.uniquePaths(5, 4)
print(res)