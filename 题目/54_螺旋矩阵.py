# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 54_螺旋矩阵.py
# @Time       ：2023/12/9 15:15
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
"""
# ================【功能：】====================
class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        cds = [1, 0, -1, 0]  # 列坐标步进方向
        rds = [0, 1, 0, -1]  # 行坐标步进方向

        # 行列当前元素数量（步进数）
        rs, cs = len(matrix), len(matrix[0])

        truns = 0  # 拐弯次数
        r, c = 0, -1 # 当前元素坐标
        elem_num = rs * cs
        result = [0] * elem_num  # 结果
        index = 0  # 当前结果下标


        while index < elem_num:
            di = truns % 4  # 步进方向下标

            # 每次拐弯， 交替使用行和列的步进
            steps = cs if truns % 2 == 0 else rs
            for i in range(steps):
                r += rds[di]
                c += rds[di]
                result[index] = matrix[r][c]
                index += 1

            # 每两次拐弯， 行列的步进数递减
            if truns % 2 == 0:
                cs -= 1
                rs -= 1

            truns += 1

        return result


s = Solution()
res = s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(res)