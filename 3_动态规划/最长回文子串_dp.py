# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 最长回文子串_dp.py
# @Time       ：2024/1/29 9:42
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
def lcs(s):
    n = len(s)
    res = []
    for i in range(n):
        for j in range(i + 1, n):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                res.append(j - i + 1)
            # else:
            #     continue
    return res

res = lcs("abaabaaba")
print(res)