# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 42_接雨水.py
# @Time       ：2023/11/16 18:56
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9
"""
# ================【功能：】====================
class Solution:
    def trap(self, height):
        if not height:
            return 0
        n = len(height)
        res = 0
        # 数组充当备忘录
        l_max = [0] * n
        r_max = [0] * n

        # 初始化base case
        l_max[0] = height[0]
        r_max[n - 1] = height[n - 1]

        # 从左往右计算
        for i in range(1, n):
            l_max[i] = max(height[i], l_max[i-1])
        # 从右往左计算
        for i in range(n - 2, -1, -1):
            r_max[i] = max(height[i], r_max[i + 1])

        print(l_max)
        print(r_max)
        # 计算
        for i in range(1, n - 1):
            res += min(l_max[i], r_max[i]) - height[i]
        return res





s = Solution()  # 1 1 2 5 6 7 10
output = s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(output)





