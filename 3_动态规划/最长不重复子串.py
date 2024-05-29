# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 最长不重复子串.py
# @Time       ：2024/1/26 11:25
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
def lls(s):
    if len(s) == 0:
        return 0
    start = 0
    max_len = 1
    for end in range(len(s)):
        wind = s[start: end + 1]
        if wind.count(s[start]) > 1:
            start += 1
            wind = s[start: end + 1]
        if wind.find(s[end]) < len(wind) - 1:
            start = wind.find(s[end]) + start
            wind = s[start: end + 1]



if __name__ == '__main__':
    res = lls("pwwkew")
    print(res)