# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 51_N皇后.py
# @Time       ：2023/12/7 18:40
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：[["Q"]]

"""
# ================【功能：】====================
class Solution:
    def __init__(self):
        self.res = []
    def solveNQueens(self, n):
        # 初始化空棋盘
        board = [['.' for j in range(n)] for i in range(n)]
        self.backtrack(board, 0)
        return len(self.res)

    def backtrack(self, board, row):
        if row == len(board):  # 触发结束条件
            self.res.append([''.join(board[i]) for i in range(len(board))])
            return
        for col in range(len(board[row])):
            if not self.isValid(board, row, col):  # 排除不合法选择
                continue

            board[row][col] = 'Q'  # 做选择
            self.backtrack(board, row + 1)  # 进入下一行做决策
            board[row][col] = '.'  # 撤销选择


    def isValid(self, board, row, col):
        n = len(board)
        # 检查列是否有皇后冲突
        for i in range(row + 1):
            if board[i][col] == 'Q':
                return False

        # 检测右上方是否有皇后冲突
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 'Q':
                return False

        # 检查左上方是否有皇后相互冲突
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        return True


s = Solution()
res = s.solveNQueens(4)
print(res)












