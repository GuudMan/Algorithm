# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 二分查找_最长递增子序列.py
# @Time       ：2024/1/24 17:05
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================

def lengthOfLIS(nums):
    top = [0] * len(nums)
    piles = 0
    for i in range(len(nums)):
        # 要处理的扑克牌
        poker = nums[i]

        # 搜索左侧边界的二分查找
        left = 0
        right = piles
        while left < right:
            mid = (left + right) // 2
            if top[mid] > poker:
                right = mid
            elif top[mid] < poker:
                left = mid + 1
            else:
                right = mid
        # 没找到合适的牌堆， 新建一堆
        if left == piles:
            piles += 1
        top[left] = poker
    return piles

res = lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
print(res)







