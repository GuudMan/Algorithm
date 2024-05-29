# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 80_删除有序数组中的重复项 II.py
# @Time       ：2023/12/19 19:37
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""
# ================【功能：】====================
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        # 快慢指针， 维护nums[0..slow]为结果子数组
        slow, fast = 0, 0
        # 记录元素重复次数
        count = 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            elif slow < fast and count < 2:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
            count += 1
            if fast < len(nums) and nums[fast] != nums[fast - 1]:
                count = 0
        return slow + 1





s = Solution()
res = s.removeDuplicates([1,1,1,2,2,3])
print(res)
