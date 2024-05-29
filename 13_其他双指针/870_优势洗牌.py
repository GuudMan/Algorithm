# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 870_优势洗牌.py
# @Time       ：2024/3/4 19:15
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定两个大小相等的数组 A 和 B，A相对于B的优势可以用满足 A[i] > B[i] 的索引i 的数目来描述。

请你返回 A 的任意排列，使其相对于B 的优势最大化。

示例 1：
输入：A = [2,7,11,15], B = [1,10,4,11]
输出：[2,11,7,15]

"""


# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
# class Solution(object):
#     def advantageCount(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         res = []
#         temp_num = nums1.copy()
#         for index, i2 in enumerate(nums2):
#             temp_i1 = []
#             for i in temp_num:
#                 if i > i2:
#                     temp_i1.append(i)
#             if len(temp_i1) <= 0:
#                 temp_i1.append(min(temp_num))
#             temp_i1.sort()
#             res.append(temp_i1[0])
#             temp_num.remove(temp_i1[0])
#         return res
class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = len(nums1)
        maxpq = []
        for i in range(n):
            maxpq.append([i, nums2[i]])
        maxpq.sort(key=lambda x: -x[1])
        print("maxpq:", maxpq)
        nums1.sort()
        left = 0
        right = n - 1
        res = [0] * n
        while maxpq:
            pair = maxpq.pop(0)
            # maxval是nums2中的最大值， i是对应索引
            i = pair[0]
            maxval = pair[1]
            if maxval < nums1[right]:
                res[i] = nums1[right]
                right -= 1
            else:
                res[i] = nums1[left]
                left += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)
so = Solution()
nums1 = [2, 0, 4, 1, 2]
nums2 = [1, 3, 0, 0, 2]
res = so.advantageCount(nums1, nums2)
print(res)
