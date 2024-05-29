# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 875_吃香蕉的最小速度.py
# @Time       ：2024/2/27 10:54
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
珂珂喜欢吃香蕉。这里有 N 堆香蕉，第i堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。
珂珂可以决定她吃香蕉的速度 K（单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉K根。如果这堆香蕉少于K根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。
珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。计算她可以在H小时内吃掉所有香蕉的最小速度K（K为整数）。

示例 1：
输入：piles = [3,6,7,11], H = 8
输出：4

示例 2：
输入：piles = [30,11,23,4,20], H = 5
输出：30

示例 3：
输入：piles = [30,11,23,4,20], H = 6
输出：23
"""
# ================【功能：】====================
class Solution(object):
    def canFinish(self, piles, speed, H):
        time = 0
        for n in piles:
            # 没吃完， 剩下的还得一个小时
            remain = 0
            if n % speed > 0:
                remain = 1
            time += (n // speed) + remain
        return time <= H

    def minEatingSpeed(self, piles, H):
        left = 1
        right = max(piles) + 1

        while left < right:
            mid = int((left + right) // 2)
            # 若小于H， 说明每次吃的太多， 因此， right = mid
            # 若大于H， 则说明每次吃的太少， 因此left = mid + 1
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
