# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 18_四数之和.py
# @Time       ：2023/9/27 16:01
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]]
（若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

示例 2：
输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]


提示：
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        result = list()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                left = j + 1
                right = len(nums) - 1
                while right > left:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        temp = [nums[i], nums[j], nums[left], nums[right]]
                        if temp not in result:
                            result.append(temp)
                        left += 1
                        right -= 1
                    if nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1

        return list(result)


if __name__ == '__main__':
    s = Solution()
    x = [2, 2, 2, 2, 2]
    y = 8
    res = s.fourSum(x, y)
    print(res)
