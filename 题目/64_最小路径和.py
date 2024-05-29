# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 64_最小路径和.py
# @Time       ：2023/12/12 19:56
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12
"""
# ================【功能：】====================
class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        memo = [[-1] * n for _ in range(m)]
        return self.dp(grid, m - 1, n - 1, memo)

    def dp(self, grid, i, j, memo):
        if i == 0 and j == 0:
            return grid[0][0]
        if i < 0 or j < 0:
            return float("inf")
        if memo[i][j] != -1:
            return memo[i][j]
        memo[i][j] = min(
            self.dp(grid, i - 1, j, memo),
            self.dp(grid, i, j - 1, memo)
        ) + grid[i][j]
        return memo[i][j]








s = Solution()
res = s.minPathSum([[0, 1], [0, 0]])
print(res)