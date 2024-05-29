# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 84_柱状图中最高的柱子.py
# @Time       ：2023/12/25 19:11
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
def largestRectangleArea(heights):
    i = 0
    max_value = 0
    stack = []
    heights.append(0)
    while i < len(heights):
        if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
            stack.append(i)
            i += 1
        else:
            now_idx = stack.pop()
            if len(stack) == 0:
                max_value = max(max_value, i * heights[now_idx])
            else:
                max_value = max(max_value, (i - stack[-1] -1) * heights[now_idx])
    return max_value


if __name__ == '__main__':
    res = largestRectangleArea([2,1,5,6,2,3])
    print(res)