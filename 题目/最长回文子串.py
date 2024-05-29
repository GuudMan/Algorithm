# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 最长回文子串.py
# @Time       ：2023/9/9 17:18
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个字符串 s，找到 s 中最长的回文子串。
如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"
"""


# ================【功能：】====================
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            s1 = self.palidrome(s, i, i)
            s2 = self.palidrome(s, i, i + 1)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res

    def palidrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]


if __name__ == '__main__':
    s = Solution()
    str1 = 'a'
    res = s.longestPalindrome(str1)
    print(res)
