# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 1011_在D天内送包裹的能力.py
# @Time       ：2024/2/27 11:50
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class Solution(object):
    def shipWithinDays(self, weights, D):
        left = 0
        right = 1
        for w in weights:
            left = max(left, w)
            right += w
        while left < right:
            mid = int((left + right) // 2)
            if self.f(weights, mid) <= D:
                right = mid
            else:
                left = mid + 1
        return left

    def f(self, weight, x):
        # 当运载能力为x时， 需要f(x)天运完所有货物
        # f(x)随着x的增加单调递减
        days = 0
        for i in range(len(weight)):
            cap = x
            while i < len(weight):
                if cap < weight[i]:
                    break
                else:
                    cap -= weight[i]
                i += 1
            days += 1
        return days


s = Solution()
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D = 5
res = s.shipWithinDays(weights, D)
print(res)
