# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 354_俄罗斯套娃信封问题.py
# @Time       ：2024/2/27 17:15
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个二维整数数组envelopes，其中envelopes[i] = [wi, hi]，表示第i个信封的宽度和高度。
当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
请计算 最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
注意：不允许旋转信封。
示例 1：
输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出：3
解释：最多信封的个数为 3, 组合为：[2,3] => [5,4] => [6,7]。
"""
# ================【功能：】====================
class Solution(object):
    def maxEnvelops(self, envelopes):
        n = len(envelopes)
        # 宽度升序排列， 如果宽度一样， 则按高度降序
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # 对高度数组， 寻找LIS
        height = [0] * n
        for i in range(n):
            height[i] = envelopes[i][1]
        print(height)
        return self.lengthofLIS(height)

    def lengthofLIS(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        res = 0
        # for i in range(len(dp)):
        #     res = max(res, dp[i])
        res = max(dp)
        return res


s = Solution()
envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
res = s.maxEnvelops(envelopes)
print(res)
