# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 303_区域和检索_数组不可变.py
# @Time       ：2024/3/9 15:54
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你输入一个整数数组nums，请你实现NumArray类：

1、NumArray(int[] nums)使用数组nums初始化对象

2、int sumRange(int i, int j)返回数组nums从索引 i到 j（i ≤ j）
范围内元素的总和，包含 i，j两点（也就是sum(nums[i], nums[i + 1], ... , nums[j])）
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # 前缀和数组
        self.preSum = [0] * (len(nums) + 1)
        for i in range(1, len(self.preSum)):
            self.preSum[i] = self.preSum[i - 1] + nums[i - 1]

    # 查询闭区间 [left, right] 的累加和
    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.preSum[right + 1] - self.preSum[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# leetcode submit region end(Prohibit modification and deletion)
