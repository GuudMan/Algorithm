# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 35_搜索插入位置.py
# @Time       ：2024/2/27 9:27
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2

示例 2:
输入: nums = [1,3,5,6], target = 2
输出: 1

示例 3:
输入: nums = [1,3,5,6], target = 7
输出: 4

"""
# ================【功能：】====================
class Solution(object):
    def searchRange(self, nums, target):
        return self.left_bound(nums, target)

    def left_bound(self, nums, target):
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((left + right) // 2)
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


s = Solution()
nums = [1, 3, 5, 6]
target = 2
res = s.searchRange(nums, target)
print(res)
