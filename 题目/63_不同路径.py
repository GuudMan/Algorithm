# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 63_不同路径.py
# @Time       ：2023/12/12 19:42
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。
"""
# ================【功能：】====================
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [[0] * n for _ in range(m)]
        return self.dp(obstacleGrid, m - 1, n - 1, memo)
    def dp(self, grid, i, j , memo):
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 1:
            # 数组越界或遇到障碍
            return 0
        if i == 0 and j == 0:
            # 起点到终点的路径就是1
            return 1
        if memo[i][j] > 0:
            return memo[i][j]

        left = self.dp(grid, i, j - 1, memo)
        upper = self.dp(grid, i - 1, j, memo)
        res = left + upper
        memo[i][j] = res
        return res


s = Solution()
res = s.uniquePathsWithObstacles([[0,1],[0,0]])
print(res)