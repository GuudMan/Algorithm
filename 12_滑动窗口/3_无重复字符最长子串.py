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
        left = 0
        right = 0
        n = len(s)
        temp = s[left: right]
        res = []
        while right < n:
            if s[right] not in temp:
                temp = s[left: right + 1]
                res.append((temp, len(temp)))
                right += 1
            else:
                left += 1
            temp = s[left: right]

        if len(res) > 0:
            res.sort(key=lambda x: x[1], reverse=True)
            result = res[0][1]
        else:
            result = 0
        return result


so = Solution()
s = "acbbaaccbbd"
res = so.lengthOfLongestSubstring(s)
print(res)