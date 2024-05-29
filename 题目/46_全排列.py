# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 46_全排列.py
# @Time       ：2023/11/30 19:06
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]

示例 3：
输入：nums = [1]
输出：[[1]]
"""
# ================【功能：】====================
class Solution:
    def __init__(self):
        self.res = []
    def permute(self, nums):
        # 记录
        track = []
        # [路径]中元素的全部表标记为true吗避免重复利用
        used = [False] * len(nums)
        self.backtrack(nums, track, used)
        return self.res

    # 路径： 记录在track中
    # 选择列表:  num中不存在track的那些元素（used[i]为false
    # 结束条件： nums中的元素全部都在track中
    def backtrack(self, nums, track, used):
        # 触发结束条件
        if len(track) == len(nums):
            self.res.append(track[:])
            return
        for i in range(len(nums)):
            # 排除不合法的选择
            if used[i]:
                # num[i]已经在track中， 跳过
                continue
            # 做选择
            track.append(nums[i])
            used[i] = True
            # 进入下一层决策树
            self.backtrack(nums, track, used)
            # 取消选择
            track.pop()
            used[i] = False











s = Solution()  # 1 1 2 5 6 7 10
output = s.permute([2, 3, 1, 1, 4])
print(output)









