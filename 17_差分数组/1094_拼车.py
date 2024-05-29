# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 1094_拼车.py
# @Time       ：2024/3/18 9:45
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）

给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengersi, fromi,
toi] 表示第 i 次旅行有 numPassengersi 乘客，接他们和放他们的位置分别是 fromi 和 toi 。
这些位置是从汽车的初始位置向东的公里数。
当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。

示例 1：
输入：trips = [[2,1,5],[3,3,7]], capacity = 4
输出：false

示例 2：
输入：trips = [[2,1,5],[3,3,7]], capacity = 5
输出：true
"""
# ================【功能：】====================


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        # 最多有1000个车站
        nums = [0] * 1001
        # 构造差分解法
        df = self.Difference(nums)

        for trip in trips:
            # 乘客数量
            val = trip[0]
            # 第trip[1]站乘客上车
            i = trip[1]
            # 第trip[2]站乘客已下车
            # 即乘客在车上的区间是[trip[1], trip[2] - 1]
            j = trip[2] - 1
            # 进行区间操作
            df.increment(i, j, val)

        res = df.result()

        # 客车自始至终都不应该超载
        for i in range(len(res)):
            if capacity < res[i]:
                return False
        return True

    # 差分数组工具类
    class Difference:
        # 差分数组
        diff = []
        """输入一个初始数组， 区间操作将在这个数组上进行"""
        def __init__(self, nums):
            assert len(nums) > 0
            self.diff = [0] * len(nums)
            # 根据初始数组构造差分数组
            self.diff[0] = nums[0]
            for i in range(1, len(nums)):
                self.diff[i] = nums[i] - nums[i - 1]

        """给闭区间[i, j]增加val（可以是负数）"""
        def increment(self, i, j, val):
            self.diff[i] += val
            if j + 1 < len(self.diff):
                self.diff[j + 1] -= val

        """返回结果数组"""
        def result(self):
            res = [0] * len(self.diff)
            # 根据差分数组构造结果数组
            res[0] = self.diff[0]
            for i in range(1, len(self.diff)):
                res[i] = res[i - 1] + self.diff[i]
            return res


# leetcode submit region end(Prohibit modification and deletion)
so = Solution()
trips = [[2, 1, 5], [3, 3, 7]]
capacity = 4
res = so.carPooling(trips, capacity)
print(res)
