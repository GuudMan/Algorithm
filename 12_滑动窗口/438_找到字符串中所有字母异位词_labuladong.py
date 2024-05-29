# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 438_找到字符串中所有字母异位词.py
# @Time       ：2024/2/28 15:08
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定两个字符串 s 和p，找到 s中所有 p的异位词子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词指由相同字母重排列形成的字符串（包括相同的字符串）。

示例 1:
输入：s = "cbaebabacd", p = "abc"
输出：[0,6]
解释：
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

示例 2:
输入：s = "abab", p = "ab"
输出：[0,1,2]
解释：
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。

s = "ababababab"
t = "aab"  [0, 2, 4, 6]
"""
# ================【功能：】====================
from collections import Counter


# class Solution:
#     def findAnagrams(self, s: str, p: str):
#         # 特殊情况判断
#         if s == "": return None
#         if len(s) < len(p): return None
#         ls = len(p)
#         record = Counter(p)
#         win = {}
#         left = 0
#         res = []
#         for r, c in enumerate(s):
#             if c not in record:
#                 win.clear()
#                 left = r + 1
#             else:
#                 win[c] = win.get(c, 0) + 1
#                 if r - left + 1 == ls:
#                     if win == record:
#                         res.append(left)
#                     win[s[left]] -= 1
#                     left += 1
#         return res

class Solution:
    def findAnagrams(self, s: str, p: str):
        if s == "": return None
        if len(s) < len(p): return None
        left = 0
        win = {}
        count_p = Counter(p)
        res = []
        for r, c in enumerate(s):
            if c not in count_p:
                win.clear()
                left = r + 1
            else:
                win[c] = win.get(c, 0) + 1
                if r - left + 1 == len(p):
                    if win == count_p:
                        res.append(left)
                    win[s[left]] -= 1
                    left += 1
        return res


so = Solution()
s = "bbbca"
t = "abc"
res = so.findAnagrams(s, t)
print(res)