# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 56_合并区间.py
# @Time       ：2023/12/11 19:00
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
示例 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2：
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

"""
# ================【功能：】====================
class Solution:
    def merge(self, intervals):
        res = []
        # start升序
        intervals.sort(key=lambda a: a[0])
        res.append(intervals[0])
        for curr in intervals[1:]:
            # 取res的引用
            last = res[-1]
            if curr[0] <= last[1]:
                last[1] = max(curr[1], last[1])
            else:
                res.append(curr)
        return res



s = Solution()
res = s.merge([[1,3],[2,6],[8,10],[15,18]])
print(res)
