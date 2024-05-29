# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 15_三数之和.py
# @Time       ：2024/2/29 20:30
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个包含n个整数的数组 nums，判断 nums 中是否存在三个元素a，b，c，使得a + b + c = 0？

请你找出所有和为0且不重复的三元组。

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
"""


# ================【功能：】====================
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        left = 0
        right = len(nums) - 1
        res = []
        while left < right:
            temp_nums = nums[left + 1: right]
            if len(temp_nums) > 0:
                for i in temp_nums:
                    if i + nums[left] + nums[right] == 0:
                        res.append([nums[left], i, nums[right]])
                        left += 1
                        right -= 1
                    elif i + nums[left] + nums[right] > 0:
                        right -= 1
                    else:
                        left += 1
            else:
                res = []
        return res


so = Solution()
nums = [0, 1, 1]
res = so.threeSum(nums)
print(res)
