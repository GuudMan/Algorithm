# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 215_数组中的第k个最大元素.py
# @Time       ：2024/3/19 19:46
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定整数数组nums和整数k，请返回数组中第k个最大的元素。

请注意，你需要找的是数组排序后的第k个最大的元素，而不是第k个不同的元素。

示例 1:

输入：[3,2,1,5,6,4] 和 k = 2
输出：5
示例 2:

输入：[3,2,3,1,2,4,5,5,6] 和 k = 4
输出：4
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 小顶堆， 堆顶是最小元素
        pq = []
        for e in nums:
            # 每个元素都要过一遍二叉堆
            heapq.heappush(pq, e)
            # 堆中元素多余k个时， 删除堆顶元素
            if len(pq) > k:
                heapq.heappop(pq)
        # pq中剩下的是nums中k个最大元素
        # 堆顶是最小的那个， 即第k个最大元素
        return pq[0]







# leetcode submit region end(Prohibit modification and deletion)
