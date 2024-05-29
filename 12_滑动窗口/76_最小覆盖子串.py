# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 76_最小覆盖子串.py
# @Time       ：2024/2/28 9:33
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个字符串s、一个字符串t，返回s中涵盖t所有字符的最小子串；如果s中不存在涵盖t所有字符的子串，则返回空字符串""。
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。

"""
# ================【功能：】====================
class Solution:
    def minWindow(self, s: str, t: str):
        left = 0
        right = 0
        ls = len(s)
        lt = len(t)
        # if lt > ls:
        #     return ""
        res = []

        while right < ls:
            temp = s[left: right + 1]
            if self.iscontain(temp, t):
                left += 1
                res.append((temp, len(temp)))
            else:
                right += 1
        print(res)
        if len(res) > 0:
            res.sort(key=lambda x: x[1], reverse=False)
            result = res[0][0]
        else:
            result = ""
        return result

    def iscontain(self, s, t):
        # s = "".join(sorted(s))
        # t = "".join(sorted(t))
        # if t in s:
        #     return True
        # else:
        #     return False
        if len(t) > len(s):
            return False
        for ti in t:
            if ti not in s:
                return False
        return True


so = Solution()
s = "ABAC"
t = "ABC"
res = so.minWindow(s, t)
print(res)












