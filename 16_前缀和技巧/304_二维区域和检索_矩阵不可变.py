# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 304_二维区域和检索_矩阵不可变.py
# @Time       ：2024/3/12 18:47
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个二维矩阵matrix，其中的一个子矩阵用其左上角坐标(row1, col1)和右下角坐标(row2, col2)来表示。

请你实现NumMatrix类：

1、NumMatrix(int[][] matrix) 给定整数矩阵matrix进行初始化

2、int sumRegion(int row1, int col1, int row2, int col2) 返回左上角(row1, col1) ，
右下角(row2, col2)所描述的子矩阵的元素总和。
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            m, n = 0, 0
        else:
            m = len(matrix)
            n = len(matrix[0])
        self.thesum = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.thesum[i + 1][j + 1] = self.thesum[i][j + 1] + self.thesum[i + 1][j] - self.thesum[i][j] + matrix[i][j]



    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int x1
        :type col1: int y1
        :type row2: int x2
        :type col2: int y2
        :rtype: int
        """
        return self.thesum[row2 + 1][col2 + 1] - self.thesum[row2 + 1][col1] - \
               self.thesum[row1][col2 + 1] + self.thesum[row1][col1]




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# leetcode submit region end(Prohibit modification and deletion)














