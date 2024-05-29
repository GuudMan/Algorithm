# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 74_搜索二维矩阵.py
# @Time       ：2023/12/18 19:14
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个满足下述两条属性的 m x n 整数矩阵：

每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for matrix_i in matrix:
            if target in matrix_i:
                return True
            else:
                continue
        return False
# leetcode submit region end(Prohibit modification and deletion)






