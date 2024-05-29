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


class Solution:
    def findAnagrams(self, s: str, p: str):
        left = 0
        right = 0
        ls = len(s)
        counter_t = Counter(p)
        res = []
        while right < ls:
            if s[right] not in counter_t:
                left = right
                right = left + 1
            else:
                if len(p) == 1:
                    temp = s[left + 1: right + 1]
                else:
                    temp = s[left: right+1]
                print(temp)
                temp_t = Counter(temp)
                if len(p) == 1:
                    flag = right - left
                else:
                    flag = right - left + 1
                if flag == len(p):
                    if temp_t == counter_t:
                        res.append(left)
                        left += 1
                        right = left + 1
                    else:
                        left += 1
                        right += 1
                else:
                    right += 1
        return res


so = Solution()
s = "acdcaeccde"
t = "c"
res = so.findAnagrams(s, t)
print(res)