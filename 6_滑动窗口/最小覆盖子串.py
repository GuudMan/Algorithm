# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 最小覆盖子串.py
# @Time       ：2024/1/24 10:24
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class Solution:
    def minSubset(self, s, target):
        left = 0
        right = 0
        n = len(s)
        window = []
        res = s
        while right < n:
            temp = s[left:right+1]
            if self.is_contain(temp, target):
               while self.is_contain(temp, target):
                   left += 1
                   if len(res) > len(temp):
                       res = temp
                   temp = s[left:right+1]
            else:
                right += 1
        return res

    def is_contain(self, A, B):
        for char in B:
            if char not in A:
                return False
        return True


s = Solution()
res = s.minSubset("ADOBACODEBANC", "ABC")
print(res)