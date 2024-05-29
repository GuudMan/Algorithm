# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 二分查找.py
# @Time       ：2024/1/24 10:13
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class Solution:
    def binary_search(self, nums, target):
        left = 0
        right = target - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid



s = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
target = 4
res = s.binary_search(nums, target)
print(res)


