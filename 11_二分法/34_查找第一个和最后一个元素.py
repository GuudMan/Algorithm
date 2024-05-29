# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 34_查找第一个和最后一个元素.py
# @Time       ：2024/2/26 19:29
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

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
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.search_left(nums, target), self.search_right(nums, target)]


    def search_left(self, nums, target):
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
        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    def search_right(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((left + right) // 2)
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if right < 0 or nums[right] != target:
            return -1
        return right


s = Solution()
nums = [5, 7, 7, 7, 7, 7, 8, 8, 10]
target = 7
res = s.searchRange(nums, target)
print(res)








