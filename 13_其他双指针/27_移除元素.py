# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 27_移除元素.py
# @Time       ：2024/2/29 20:11
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个数组nums和一个值val，你需要原地移除所有数值等于 val的元素，并返回移除后数组的新长度。

你必须仅使用O(1)额外空间并原地修改输入数组。元素的顺序可以改变，你不需要考虑数组中超出新长度后面的元素。
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] == val:
                right += 1
            else:
                nums[left] = nums[right]
                left += 1
                right += 1
        return left

so = Solution()
nums = [3,2,2,3]
val = 3
res = so.removeElement(nums, val)
print(res)