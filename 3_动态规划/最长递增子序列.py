# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 最长递增子序列.py
# @Time       ：2024/1/24 16:43
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class Solution:
    def maxSubset(self, nums):
        self.dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    self.dp[i] = max(self.dp[i], self.dp[j] + 1)
        print(self.dp)
        return max(self.dp)


s = Solution()
res = s.maxSubset([10, 9, 2, 5, 3, 7, 101, 18])
print(res)