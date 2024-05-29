# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 盛水最多的容器.py
# @Time       ：2023/9/19 19:38
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。
"""
# ================【功能：】====================


class Solution:
    def maxArea(self, height) -> int:
        if not isinstance(height, list):
            return 0
        if len(height) <= 1:
            return 0
        area = 0
        len_h = len(height)
        right = len_h - 1
        left = 0
        while right >= left:
            new_area = min(height[right], height[left]) * (right - left)
            if new_area > area:
                area = new_area
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return area


if __name__ == '__main__':
    s = Solution()
    x_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # x_list = 1, 1
    res = s.maxArea(x_list)
    print(res)
