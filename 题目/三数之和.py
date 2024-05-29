# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 三数之和.py
# @Time       ：2023/9/5 19:25
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个整数数组 nums ，
判断是否存在三元组 [nums[i], nums[j], nums[k]]
满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
你返回所有和为 0 且不重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。

示例 2：
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。

示例 3：
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
"""


# ================【功能：】====================


class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        for index in range(len(nums)):
            j = len(nums) - 1
            target = - nums[index]
            i = index + 1
            while j - i >= 1:
                if nums[i] + nums[j] == target:
                    if [nums[index], nums[i], nums[j]] not in res:
                        res.append([nums[index], nums[i], nums[j]])
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                else:
                    continue
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.threeSum([-1,0,1,2,-1,-4])
    print(res)
