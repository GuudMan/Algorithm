# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 34_在排序数组中找到第一个和最后一个位置.py
# @Time       ：2023/11/9 19:05
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。
请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]
"""


# ================【功能：】====================
class Solution:
    def searchRange(self, nums, target: int):
        if nums == [] or target not in nums:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        res = []
        while left <= right:
            if nums[left] < target:
                left += 1
            elif nums[left] == target:
                if left not in res:
                    res.append(left)
                if nums[right] > target:
                    right -= 1
                elif nums[right] == target:
                    res.append(right)
                    break

        return res


s = Solution()
output = s.searchRange([], 8)
print(output)
