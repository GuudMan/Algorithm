# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 48_旋转图像.py
# @Time       ：2023/11/30 19:39
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
"""
# ================【功能：】====================
class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        # 先沿着对角线反转二维矩阵
        for i in range(n):
            for j in range(i, n):
                # swap matrix[i][j] -> matrix[j][j]
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        # 反转二维矩阵每一行
        for row in matrix:
            self.reverse(row)
        return matrix

    def reverse(self, arr):
        i, j = 0, len(arr) - 1
        while j > i:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1


s = Solution()
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
res = s.rotate(matrix=matrix)
print(res)
