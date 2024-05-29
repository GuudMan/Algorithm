# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 392_判断子序列.py
# @Time       ：2024/2/27 10:19
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class Solution(object):
    def isSubsequence(self, s1, s2):
        i = 0
        j = 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
            j += 1
        return i == len(s1) or j == len(s2)




s = Solution()
s2 = "abc"
s1 = "assdbdfc"
res = s.isSubsequence(s1, s2)
print(res)








