# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 无重复字符的最长子串.py
# @Time       ：2023/9/4 19:26
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


# ================【功能：】====================

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 0:
            return 0
        lookup = set()
        len_s = len(s)
        maxsize, i, j = 0, 0, 0
        while i < len_s and j < len_s:
            if s[j] not in lookup:
                lookup.add(s[j])
                j += 1
                maxsize = max(maxsize, j - i)
                print(maxsize)
            else:
                lookup.remove(s[i])
                i += 1
        return maxsize


if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLongestSubstring("abcabcbb")
    print(res)
