# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 567_字符串的排列.py
# @Time       ：2024/2/29 18:54
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str):
        if s2 == "": return False
        if len(s2) < len(s1): return False
        left = 0
        count_s = Counter(s1)
        win = {}
        res = []
        for r, c in enumerate(s2):
            if c not in count_s:
                win.clear()
                left = r + 1
            else:
                win[c] = win.get(c, 0) + 1
                if r - left + 1 == len(s1):
                    if win == count_s:
                        return True

                    win[s2[left]] -= 1
                    left += 1
        return False



so = Solution()
s1 = "abc"
s2 = "bbbca"
res = so.checkInclusion(s1, s2)
print(res)