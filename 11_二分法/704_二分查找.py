# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 704_二分查找.py
# @Time       ：2024/2/26 19:09
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
"""
# ================【功能：】====================
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            # mid = int((left + right) // 2)
            mid = int(left + (right - left) / 2)
            print(mid)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1



s = Solution()
nums = [-1,0,3,5,9,12]
target = 13
res = s.search(nums, target)
print(res)




