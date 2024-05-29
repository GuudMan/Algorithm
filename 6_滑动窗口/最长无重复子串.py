# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 最长无重复子串.py
# @Time       ：2024/1/24 14:33
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class Solution:
    def unique_set(self, s):
        left = 0
        right = 0
        n = len(s)
        temp = []
        res = ""
        while right < n:
            if s[right] not in s[left: right]:
                temp = s[left:right+1]
                right += 1
            else:
                if len(temp) > len(res):
                    res = "".join(temp)
                temp = []
                left += 1
                # right += 1
        return len(res)


s = Solution()
res = s.unique_set("abcabecbfgb")
print(res)