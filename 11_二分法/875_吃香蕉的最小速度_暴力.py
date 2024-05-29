# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 875_吃香蕉的最小速度_暴力.py
# @Time       ：2024/2/27 11:28
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class Solution(object):
    def canFinish(self, piles, speed, H):
        time = 0
        for n in piles:
            remain = 0
            if n % speed > 0:
                remain = 1
            time += n // speed + remain
        return time <= H


    def minEatingSpeed(self, piles, H):
        max_s = max(piles)
        for speed in range(1, max_s + 1):
            if self.canFinish(piles, speed, H):
                return speed
        return max_s


s = Solution()
piles = [3, 6, 7, 11]
H = 8
res = s.minEatingSpeed(piles, H)
print(res)