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
def dp(nums, start):
    if start >= len(nums):
        return 0
    # max(// 不抢， 去下家  // 抢， 去下下家)
    res = max(dp(nums, start + 1), nums[start] + dp(nums, start + 2))
    return res


def rob(nums):
    return dp(nums, 0)


nums = [2, 7, 9, 3, 1]
res = rob(nums)
print(res)
