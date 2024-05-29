# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 28_找出字符串中第一个匹配项的下标.py
# @Time       ：2023/10/31 19:36
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你两个字符串 haystack 和 needle ，
请你在 haystack 字符串中找出 needle
字符串的第一个匹配项的下标（下标从 0 开始）。
如果 needle 不是 haystack 的一部分，则返回  -1 。

示例 1：

输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。
示例 2：

输入：haystack = "leetcode", needle = "leeto"
输出：-1
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。

"""
# ================【功能：】====================
from gettext import find


class Solution:
    def strStr(self, haystack: str, needle: str):
        # return haystack.find(needle)
        ln = len(needle)
        if needle not in haystack:
            return -1
        for i in range(len(haystack) - ln + 1):
            if haystack[i: i + ln] == needle:
                return i





s = Solution()
input = "sadbutsad"
str2 = "sad"
output = s.strStr(input, str2)
print(output)
