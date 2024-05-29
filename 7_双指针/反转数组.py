# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 反转数组.py
# @Time       ：2024/1/24 15:49
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class Solution:
    def reverse(self, nums):
        n = len(nums)
        left = 0
        right = n - 1
        while right > left:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
            left += 1
        return nums


s = Solution()
res = s.reverse([-1, 0, 1, 2, 3])
print(res)