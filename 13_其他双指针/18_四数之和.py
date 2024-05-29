# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 18_四数之和.py
# @Time       ：2024/3/4 18:47
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""


# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            temp = nums[i + 1:]
            target_three = target - num
            res_three = self.threeSum(temp, target_three)
            if len(res_three):
                for res_i in res_three:
                    res_i.append(num)
                    if res_i not in res:
                        res.append(res_i)
        return res

    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        # nums.sort()
        res = []
        for i, num in enumerate(nums):
            temp = nums[i + 1:]
            target_two = target - num
            res_two = self.twoSum(temp, target_two)
            if len(res_two) > 0:
                for res_i in res_two:
                    res_i.append(num)
                    if res_i not in res:
                        res.append(res_i)
            # res.append([res_three, num])
        return res

    def twoSum(self, nums, target):
        # nums.sort()
        left = 0
        res = []
        right = len(nums) - 1
        while left < right:
            temp = nums[left] + nums[right]
            if temp == target:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
            elif temp > target:
                right -= 1
            else:
                left += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)
so = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
res = so.fourSum(nums, target)
print(res)
