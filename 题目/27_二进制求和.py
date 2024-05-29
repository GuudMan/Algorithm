# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 27_二进制求和.py
# @Time       ：2023/12/14 18:45
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
示例 1：
输入:a = "11", b = "1"
输出："100"

示例 2：
输入：a = "1010", b = "1011"
输出："10101"
"""
# ================【功能：】====================
import re


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        aa = 0
        for index, i in enumerate(a):
            aa += int(i) * 2 ** (len(a) - index - 1)
        b = list(b)
        bb = 0
        for index, i in enumerate(b):
            bb += int(i) * 2 ** (len(b) - index - 1)
        cc = aa + bb
        if cc == 0:
            return "0"
        rs = []
        while cc:
            yushu = cc % 2
            cc = cc // 2
            rs.append(yushu)
        rs.reverse()
        return "".join(str(i) for i in rs)






s = Solution()
res = s.addBinary("0", "0")
print(res)