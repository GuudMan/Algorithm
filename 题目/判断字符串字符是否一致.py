# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 判断字符串字符是否一致.py
# @Time       ：2023/8/14 19:28
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定两个字符串，str1，str2，判断两个字符串中出现的字符是否全部种类一样，数量一样。
例如：
str1 = “apple”, str2 = “paple”, 返回 True;
str1 = “pear”, str2 = “bears”, 返回 False。
"""


# ================【功能：】====================


def two_string(str1, str2):
    if str1 is None or str2 is None:
        return False
    if len(str1) <= 0 or len(str2) <= 0:
        return False
    if len(str1) != len(str2):
        return False
    print(str1)
    str1_list = sorted(list(str1))
    print(str1_list)
    str2_list = sorted(list(str2))
    print(str2_list)
    if str1_list == str2_list:
        return True


def two_string2(str1, str2):
    if str1 is None or str2 is None:
        return False
    if len(str1) <= 0 or len(str2) <= 0:
        return False
    if len(str1) != len(str2):
        return False
    i, map = 0, [0]
    while i < 256:
        map.append(0)
        i += 1
    for i in range(0, len(str1)):
        map[ord(str1[i])] += 1
    for i in range(0, len(str1)):
        if map[ord(str2[i])] == 0:
            return False
    return True


if __name__ == '__main__':
    str1 = "apple"
    str2 = "paple"
    res = two_string2(str1, str2)
    print(res)
