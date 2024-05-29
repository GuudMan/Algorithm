# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 两数之和.py
# @Time       ：2024/1/24 15:43
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class Solution:
    def num_sum(self, nums, target):
        left = 0
        n = len(nums)
        right = n - 1
        res = []
        while right > left:
            if nums[right] + nums[left] == target:
                res.append(left + 1)
                res.append(right + 1)
                return res
            elif nums[right] + nums[left] > target:
                right -= 1
            elif nums[right] + nums[left] < target:
                left += 1
        return res


s = Solution()
res = s.num_sum([-1, 0, 1, 2, 3, 5, 6, 7, 11, 14, 19], 9)
print(res)