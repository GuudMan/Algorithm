# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 77_组合.py
# @Time       ：2023/12/19 18:35
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。

示例 1：
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

示例 2：
输入：n = 1, k = 1
输出：[[1]]
"""
# ================【功能：】====================

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        n_list = list(range(1, n + 1))
        left = 0
        right = left + k
        res = []
        while right < n:
            res_i = []
            for i in range(left, right):
                res_i.append(n_list[i])
            left += 1


        return res


s = Solution()
res = s.combine(4, 2)
print(res)



