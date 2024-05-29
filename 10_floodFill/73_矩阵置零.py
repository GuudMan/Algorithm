# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 73_矩阵置零.py
# @Time       ：2024/2/26 15:44
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""


# ================【功能：】====================

def inArea(matrix, x, y):
    m = len(matrix)
    n = len(matrix[0])
    if x >= 0 and x < m and y >= 0 and y < n:
        return True
    else:
        return False
def mainfill(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m + 1):
        for j in range(n + 1):
            fill(matrix, i, j)
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == float('inf'):
                matrix[i][j] = 0
    return matrix

def fill(matrix, x, y):

    if not inArea(matrix, x, y):
        return
    m = len(matrix)
    n = len(matrix[0])

    if matrix[x][y] == 0:
        # 所在的行
        for i in range(n):
            if matrix[x][i] != 0:
                matrix[x][i] = float('inf')
        for j in range(m):
            if matrix[j][y] != 0:
             matrix[j][y] =  float('inf')
    return matrix


res = mainfill([[1,1,1],[1,0,1],[1,1,1]])
print(res)
