# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 36_有效的数独.py
# @Time       ：2023/11/9 19:29
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
有效的数独
请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）


注意：

一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
空白格用 '.' 表示。
"""
# ================【功能：】====================

class Solution:
    def isValidSudoku(self, board):
        raw = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        col = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        cell = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        for i in range(9):
            for j in range(9):
                num = (3*(i//3) + j//3)
                temp = board[i][j]
                if temp != '.':
                    if temp not in raw[i] and temp not in col[j] and temp not in cell[num]:
                        raw[i][temp] = 1
                        col[j][temp] = 1
                        cell[num][temp] = 1
                    else:
                        return False
        return True


s = Solution()
output = s.isValidSudoku([[]])
print(output)