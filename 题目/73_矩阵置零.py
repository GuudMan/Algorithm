# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 73_矩阵置零.py
# @Time       ：2023/12/18 18:55
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
"""
# ================【功能：】====================
class Solution:
    def zeroize(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    # 将所在行的所有非0值标记为None
                    for i in range(n):
                        if matrix[r][i] != 0:
                            matrix[r][i] = None
                    # 将所在列的所有非0值标记为None
                    for j in range(m):
                        if matrix[j][c] != 0:
                            matrix[j][c] = None
        for r in range(m):
            for c in range(n):
                if matrix[r][c] is None:
                    matrix[r][c] = 0
        return matrix







s = Solution()
matrix = [
    [0, 1, 1, 0],
    [1, 1, 1, 2],
    [1, 2, 1, 1],
]
res = s.zeroize(matrix)
print(res)