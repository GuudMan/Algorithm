# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 283_移动零.py
# @Time       ：2024/2/29 20:18
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个数组nums，编写一个函数将所有0移动到数组的末尾，必须在原数组上操作，同时保持非零元素的相对顺序。

示例：

输入：[0,1,0,3,12]
输出：[1,3,12,0,0]
"""


# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def moveZeroes(self, nums):

        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] == 0:
                right += 1
            else:

                nums[left] = nums[right]
                left += 1
                right += 1
        for i in range(left, right):
            nums[i] = 0
        return nums


so = Solution()
nums = [0, 1, 0, 3, 12]
res = so.moveZeroes(nums)
print(res)
