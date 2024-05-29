# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 26_删除有序数组中的重复项.py
# @Time       ：2024/2/29 19:56
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个有序数组nums，请你原地删除重复出现的元素，使每个元素只出现一次，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用O(1)额外空间的条件下完成。
"""


# ================【功能：】====================
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] == nums[left]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1
        return nums[: left + 1]



so = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
res = so.removeDuplicates(nums)
print(res)
