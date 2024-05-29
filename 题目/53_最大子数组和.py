# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 53_最大子数组和.py
# @Time       ：2023/12/7 19:10
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23
"""


# ================【功能：】====================

class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * n
        # 第一个元素前面没有子数组
        dp[0] = nums[0]
        # 状态转移方程
        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        # 得到nums的最大子数组
        res = float('-inf')
        for i in range(n):
            res = max(res, dp[i])
        return res



s = Solution()
res = s.maxSubArray([-2, 10, -3, 4, -1, 2, 1, -5, 4])
print(res)
