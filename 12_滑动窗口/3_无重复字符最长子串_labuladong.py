# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 3_无重复字符最长子串.py
# @Time       ：2024/2/28 11:23
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        window = {}
        left = right = 0
        res = 0  # 记录结果
        while right < len(s):
            c = s[right]
            right += 1
            # 对窗口内数据的一系列更新
            window[c] = window.get(c, 0) + 1
            # 判断左侧窗口是否要收缩
            while window[c] > 1:
                d = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                window[d] -= 1
            # 在这里更新答案
            res = max(res, right - left)
        return res



so = Solution()
s = "abcabcbb"
res = so.lengthOfLongestSubstring(s)
print(res)