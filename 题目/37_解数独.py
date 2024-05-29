# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 37_解数独.py
# @Time       ：2023/11/13 19:09
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：

编写一个程序，通过填充空格来解决数独问题。

数独的解法需 遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示。

"""


# ================【功能：】====================
class Solution:
    def solveSudoku(self, board):
        self.backtrack(board, 0, 0)

    def backtrack(self, board, i, j):
        m, n = 9, 9
        if j == n:
            # 穷举到最后一列的话就换下一行重新开始
            return self.backtrack(board, i + 1, 0)
        if i == m:
            # 找到一个可行解
            return True

        if board[i][j] != '.':
            # 如果有预设数字， 不用穷举
            return self.backtrack(board, i, j + 1)

        for ch in range(1, 10):
            ch = str(ch)
            # 如果遇到不合法的数字， 则跳过
            if not self.isValid(board, i, j, ch):
                continue

            board[i][j] = ch
            # 如果找到一个可行解， 立即结束
            if self.backtrack(board, i, j + 1):
                return True
            board[i][j] = '.'
        # 穷举完1-9， 依然没有找到可行解， 此路不通
        return False

    def isValid(self, board, r, c, n):
        for i in range(9):
            # 判断行是否重复
            if board[r][i] == n:
                return False
            # 判断列是否重复
            if board[i][c] == n:
                return False
            # 判断3×3方框是否重复
            if board[(r // 3) * 3 + i // 3][(c // 3) * 3 + i % 3] == n:
                return False
        return True
