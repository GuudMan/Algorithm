# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 239_滑动窗口最大值.py
# @Time       ：2024/2/29 19:06
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个整数数组nums，有一个大小为 k的滑动窗口从数组的最左侧移动到数组的最右侧，返回滑动窗口中的最大值。

滑动窗口每次只向右移动一位，你只可以看到在滑动窗口内的k 个数字。

示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

 maxSlidingWindow
"""
# ================【功能：】====================
# class Solution:
#     def maxSlidingWindow(self, nums, k):
#         if len(nums) <= 0: return []
#         if len(nums) < k: return [max(nums)]
#         steps = len(nums) - k + 1
#         res = []
#         for step in range(steps):
#             temp = nums[step: step + k]
#             res.append(max(temp))
#         return res
import collections


# class Solution:
#     class MonotonicQueue:
#         def __init__(self):
#             self.q = []
#         def push(self, n):
#             while self.q and self.q[-1] < n:
#                 self.q.pop()
#             self.q.append(n)
#         def max(self):
#             return self.q[0]
#
#         def pop(self, n):
#             if n == self.q[0]:
#                 self.q.pop(0)
#
#
#
#     def maxSlidingWindow(self, nums, k):
#         window = self.MonotonicQueue()
#         res = []
#         for i in range(len(nums)):
#             if i < k - 1:
#                 window.push(nums[i])
#             else:
#                 window.push(nums[i])
#                 res.append(window.max())
#                 window.pop(nums[i - k + 1])
#         return res

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []

        res = []
        window = deque()

        for i, num in enumerate(nums):
            # 维护窗口大小为k
            if window and window[0] == i - k:
                window.popleft()

            # 保持窗口单调递减，窗口头部为当前窗口的最大值
            while window and nums[window[-1]] < num:
                window.pop()

            window.append(i)
            # 窗口满k时将当前最大值添加到结果列表
            if i >= k - 1:
                res.append(nums[window[0]])
        return res


so = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
res = so.maxSlidingWindow(nums, k)
print(res)
