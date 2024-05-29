# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 判断是否包含排列.py
# @Time       ：2024/1/24 14:10
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class Solution:
    def isSubset(self, s, target):
        left = 0
        right = 0
        n = len(s)
        while right < n:
            temp = s[left:right + 1]
            if self.is_contain(temp, target):
                while self.is_contain(temp, target):
                    if len(temp) == len(target):
                        return True
                    left += 1
                    temp = s[left:right + 1]
            else:
                right += 1
        return False

    def is_contain(self, t_s, t_t):
        # if len(t_s) == len(t_t):
        for i in t_t:
            if i not in t_s:
                return False
        return True
        # else:
        #     return False

s = Solution()
res = s.isSubset("cbaebabacd", "abc")
print(res)



