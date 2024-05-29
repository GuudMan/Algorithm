# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 寻找两个正序数组的中位数.py
# @Time       ：2023/9/9 17:02
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出并返回这两个正序数组的 中位数 。
示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
"""

class Solution:
    def twoListMiddle(self, nums1, nums2):
        if nums1 and nums2 is None:
            return None
        if nums1 is not None and nums2 is None:
            len_l1 = len(nums1) - 1
            if len_l1 % 2 == 0:
                index = len_l1 // 2
                return nums1[index]
            else:
                s1 = index = len_l1 // 2
                s2 = index = len_l1 // 2 + 1
                return (nums1[s1] + nums1[2]) / 2
        if nums1 is None and nums2 is  not None:
            len_l2 = len(nums2) - 1
            if len_l2 % 2 == 0:
                index = len_l2 // 2
                return nums1[index]
            else:
                s1 = index = len_l2 // 2
                s2 = index = len_l2 // 2 + 1
                return (nums2[s1] + nums2[2]) / 2
        if nums1 is not None and nums2 is not None:
            l12 = nums1 + nums2
            l12.sort()
            print(l12)
            len_l12 = len(l12) - 1
            if len_l12 % 2 == 0:
                index = len_l12 // 2
                print(index)
                return l12[index]
            else:
                s1 = index = len_l12 // 2
                s2 = index = len_l12 // 2 + 1
                return (l12[s1] + l12[s2]) / 2


if __name__ == '__main__':
    s = Solution()
    l1 = [1, 3]
    l2 = [2]
    res = s.twoListMiddle(l1, l2)
    print(res)
