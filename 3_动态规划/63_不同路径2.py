# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 63_不同路径2.py
# @Time       ：2024/1/16 20:34
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        self.memo = [[0] * n for _ in range(m)]
        return self.dp(m - 1, n - 1, obstacleGrid)
    def dp(self, i, j, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0 or obstacleGrid[i][j] == 1 or i >= m or j >= n:
            return 0
        if self.memo[i][j] > 0:
            return self.memo[i][j]
        self.memo[i][j] = self.dp(i - 1, j, obstacleGrid) + self.dp(i, j - 1, obstacleGrid)
        return self.memo[i][j]

# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
res = s.uniquePathsWithObstacles([[1]])
print(res)