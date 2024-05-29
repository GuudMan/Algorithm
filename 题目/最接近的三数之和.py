# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 最接近的三数之和.py
# @Time       ：2023/9/26 19:12
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。
请你从 nums 中选出三个整数，使它们的和与 target 最接近。
返回这三个数的和。
假定每组输入只存在恰好一个解。
示例 1：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
示例 2：
输入：nums = [0,0,0], target = 1
输出：0

提示：
3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""


# ================【功能：】====================
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        if len(nums) < 3:
            return sum(nums)
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 1):
            j0 = i + 1
            jn = len(nums) - 1
            while jn > j0:
                temp = nums[i] + nums[j0] + nums[jn]
                if abs(temp - target) < abs(ans - target):
                    ans = temp
                if temp > target:
                    jn -= 1
                else:
                    j0 += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    x_list = [-1, 2, 1, -4]
    target = 1
    res = s.threeSumClosest(x_list, target)
    print(res)
