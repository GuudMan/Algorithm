# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : house_robber.py
# @Time       ：2024/2/19 9:05
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
def robRange(nums, start, end):
    n = len(nums)
    dp_i_1 = 0
    dp_i_2 = 0
    dp_i = 0
    for i in range(end, start - 1, -1):
        dp_i = max(dp_i_1, nums[i] + dp_i_2)
        dp_i_2 = dp_i_1
        dp_i_1 = dp_i
    return dp_i


def rob(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    return max(robRange(nums, 0, n - 2), robRange(nums, 1, n - 1))



nums = [2, 3, 2]
res = rob(nums)
print(res)
