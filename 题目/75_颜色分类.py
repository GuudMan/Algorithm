# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 75_颜色分类.py
# @Time       ：2023/12/18 19:31
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。

示例 1：

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
示例 2：

输入：nums = [2,0,1]
输出：[0,1,2]
提示：

n == nums.length
1 <= n <= 300
nums[i] 为 0、1 或 2
进阶：
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        second = 0
        n = len(nums)
        for i in nums:
            if i == 0:
                left += 1
            elif i == 1:
                second += 1
            else:
                continue
        for i in range(left):
            nums[i] = 0
        for i in range(left, left + second):
            nums[i] = 1
        for i in range(left + second, n):
            nums[i] = 2

# leetcode submit region end(Prohibit modification and deletion)
