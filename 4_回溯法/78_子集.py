# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 78_子集.py
# @Time       ：2024/1/23 19:55
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。



示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]

"""
# ================【功能：】====================
class Solution:
    def subsets(self, nums):
        self.res = []
        track = []
        self.backtrack(nums, 0, track)
        return self.res

    def backtrack(self, nums, start, track):
        # track.sort()
        # if track not in self.res:
        self.res.append(track[:])
        for i in range(start, len(nums)):
            if nums[i] in track:
                continue
            track.append(nums[i])
            self.backtrack(nums, i + 1, track)
            track.pop()



s = Solution()
res = s.subsets([1, 2, 3])
print(res)