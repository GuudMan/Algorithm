# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 875_吃香蕉最小速度_二分.py
# @Time       ：2024/2/27 11:41
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
        left = 0
        right = max(piles)
        while left < right:
            mid = int((left + right) // 2)
            if self.canFinish(piles, mid, H):
                right = mid
            else:
                left = mid + 1
        return left



s = Solution()
piles = [3, 6, 7, 11]
H = 8
res = s.minEatingSpeed(piles, H)
print(res)