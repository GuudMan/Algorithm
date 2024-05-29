# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 11_剩最多水的容器.py
# @Time       ：2024/3/4 20:09
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你n个非负整数a1，a2，...，an，其中每个数代表坐标中的一个点 (i, ai)。
在坐标内画n条垂直线，垂直线i 的两个端点分别为 (i, ai)和(i, 0)。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
"""


# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            temp = min(height[left], height[right]) * (right - left)
            if temp > res:
                res = temp
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res



# leetcode submit region end(Prohibit modification and deletion)
so = Solution()
nums1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
res = so.maxArea(nums1)
print(res)
