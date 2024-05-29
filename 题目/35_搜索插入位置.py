# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 35_搜索插入位置.py
# @Time       ：2023/11/9 19:21
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
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
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if nums == []:
            return 0
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)


s = Solution()
output = s.searchInsert([1, 3, 5, 6], 7)
print(output)
