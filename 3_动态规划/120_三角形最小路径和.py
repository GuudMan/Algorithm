# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 120_三角形最小路径和.py
# @Time       ：2024/1/18 19:05
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
三角形最小路径和
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        rows = len(triangle)
        cross = len(triangle[-1])
        self.memo = [[float('inf')] * cross for _ in range(rows)]
        # for i in range(rows):
        #     for j in range(len(triangle[i])):
        #         self.memo[i][j] = float('inf')
        # return self.dp(rows - 1, cross - 1, triangle)
        res = []
        for i in range(cross):
            res.append(self.dp(rows - 1, i, triangle))
        return min(res)

    def dp(self, row, cross, triangle):
        if row == 0 and cross == 0:
            # return triangle[0][0]
            self.memo[row][cross] = triangle[0][0]
            return triangle[0][0]
        # if self.memo[row, cross]
        if cross == 0:
            self.memo[row][cross] = self.dp(row - 1, cross, triangle) + triangle[row][cross]
        elif cross < row:
            self.memo[row][cross] = min(self.dp(row - 1, cross - 1, triangle), self.dp(row - 1, cross, triangle)) \
                                    + triangle[row][cross]
        elif cross == row:
            self.memo[row][cross] = self.dp(row - 1, cross - 1, triangle) + triangle[row][cross]
        if self.memo[row][cross] < float('inf'):
            return self.memo[row][cross]
        return min(self.memo[-1])






# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
# res = s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
res = s.minimumTotal([[1],[-2,-5],[3,6,9],[-1,2,4,-3]])
print(res)