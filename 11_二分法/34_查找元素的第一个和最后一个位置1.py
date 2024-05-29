# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 34_查找元素的第一个和最后一个位置1.py
# @Time       ：2024/2/27 9:06
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class Solution(object):
    def searchRange(self, nums, target):
        return [self.search_left(nums, target), self.search_right(nums, target)]

    def search_left(self, nums, target):
        left = 0
        right = len(nums)
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
        right = len(nums)
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
