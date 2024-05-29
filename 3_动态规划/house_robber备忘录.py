# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : house_robber.py
# @Time       ：2024/2/19 9:05
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class ROB():
    def __init__(self, nums):
        self.nums = nums
        self.memo = [-1] * len(self.nums)
    def rob(self):
        return self.dp(self.nums, 0)

    def dp(self, nums, start):
        if start >= len(nums):
            return 0
        # 避免重复计算
        if self.memo[start] != -1:
            return self.memo[start]

        res = max(self.dp(nums, start + 1), nums[start] + self.dp(nums, start + 2))

        # 存入备忘录
        self.memo[start] = res
        return res


nums = [2, 7, 9, 3, 1]
rob = ROB(nums)
res = rob.rob()
print(res)
