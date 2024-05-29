# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 560_和为 K 的子数组.py
# @Time       ：2024/3/12 19:30
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个整数数组nums和一个整数 k，请你统计并返回该数组中和为 k的连续子数组的个数。

示例 1：

输入：nums = [1,1,1], k = 2
输出：2
"""


# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
# class Solution(object):
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         n = len(nums)
#         preSum = {}
#         preSum[0] = 1
#         res = 0
#         sum0_i = 0
#         for i in range(n):
#             sum0_i += nums[i]
#             sum0_j = sum0_i - k
#             if sum0_j in preSum.keys():
#                 res += preSum.get(sum0_j)
#             preSum[sum0_i] = preSum.get(sum0_i, 0) + 1
#         return res


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0
        res = {}
        res[0] = 1
        sum_i, sum_j, ans = 0, 0, 0
        for i in range(len(nums)):
            sum_i += nums[i]
            sum_j = sum_i - k
            if sum_j in res:
                ans += res[sum_j]
            if sum_i not in res:
                res[sum_i] = 0
            res[sum_i] += 1
        return ans



# leetcode submit region end(Prohibit modification and deletion)
so = Solution()
nums = [1, 1, 1]
res = so.subarraySum(nums, 2)
print(res)
