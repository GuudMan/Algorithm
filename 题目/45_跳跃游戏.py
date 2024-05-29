# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 45_跳跃游戏.py
# @Time       ：2023/11/28 19:23
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

0 <= j <= nums[i]
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。


示例 1:

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
示例 2:

输入: nums = [2,3,0,1,4]
输出: 2
"""


# ================【功能：】====================
# class Solution:
#     def jump(self, nums):
#         size = len(nums)
#
#         end = 0  # 上一步可达位置
#         far = 0  # 当前步的下一步的最远距离
#         ans = 0  # 当前步数
#
#         for i in range(size - 1):
#             # 计算当前可达到的最远距离
#             if i + nums[i] > far:
#                 far = i + nums[i]
#
#             # 上一步已经迈完了
#             if i == end:
#                 ans += 1
#                 end = far
#         return ans


class Solution:
    def jump(self, nums):
        # n = len(nums)
        # end, farthest, jumps = 0, 0, 0
        # for i in range(n - 1):
        #     farthest = max(nums[i] + i, farthest)
        #     if end == i:
        #         jumps += 1
        #         end = farthest
        # return jumps
        n = len(nums)
        i = 0
        jump = 0
        while i != n - 1:
            step_range = nums[i + 1: i + 1 + nums[i]]

            if step_range:
                far = max(step_range)
                jump += 1
            else:
                far = 0
            if i + far >= n:
                break
            i = nums.index(far)
        return jump


s = Solution()  # 1 1 2 5 6 7 10
output = s.jump([2,3,1,1,4])
print(output)
