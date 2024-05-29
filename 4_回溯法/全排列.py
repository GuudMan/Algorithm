# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 全排列.py
# @Time       ：2024/1/23 19:20
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================

def permute(nums):
    result = []
    def backtrack(nums, track):
        if len(track) == len(nums):
            temp = track.copy()
            result.append([temp])
            return

        for i in nums:
            if i in track:
                continue
            track.append(i)
            backtrack(nums, track)
            track.pop()

    track = []
    backtrack(nums, track)
    return result

res = permute([1, 2, 3])
print(res)