# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 42_接雨水.py
# @Time       ：2024/3/4 20:20
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定 n个非负整数表示每个宽度为1的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，
在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
"""


# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
# 暴力法超时
# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         n = len(height)
#         res = 0
#         for i in range(n - 1):
#             l_max = 0
#             r_max = 0
#             # 找到右边最高的柱子
#             for j in range(i, n):
#                 r_max = max(r_max, height[j])
#             # 找到左边最高的柱子
#             for j in range(i, -1, -1):
#                 l_max = max(l_max, height[j])
#             res += min(l_max, r_max) -height[i]
#         return res

# 备忘录
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 0: return 0
        n = len(height)
        res = 0
        l_max = [0] * n
        r_max = [0] * n
        # 初始化
        l_max[0] = height[0]
        r_max[n -1] = height[n - 1]
        # 从左往右计算l_max
        for i in range(1, n):
            l_max[i] = max(height[i], l_max[i - 1])
            print(l_max)
        print('------')
        # 从右往左计算r_max
        for i in range(n - 2, -1, -1):
            r_max[i] = max(height[i], r_max[i + 1])
            print(r_max)
        # 计算答案

        for i in range(1, n - 1):
            res += min(l_max[i], r_max[i]) - height[i]
        return res

# leetcode submit region end(Prohibit modification and deletion)
so = Solution()
nums1 = [4, 2, 0, 3, 2, 5]
res = so.trap(nums1)
print(res)
