# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 名字的漂亮度.py
# @Time       ：2024/1/29 18:30
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
描述
给出一个字符串，该字符串仅由小写字母组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。
每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个不同字母拥有相同的“漂亮度”。字母忽略大小写。

给出多个字符串，计算每个字符串最大可能的“漂亮度”。

本题含有多组数据。

数据范围：输入的名字长度满足


输入描述：
第一行一个整数N，接下来N行每行一个字符串
输出描述：
每个字符串可能的最大漂亮程度

示例1
输入：
2
zhangsan
lisi
输出：
192
101
说明：
对于样例lisi，让i的漂亮度为26，l的漂亮度为25，s的漂亮度为24，lisi的漂亮度为25+26+24+26=101.
"""
# ================【功能：】====================

n = input()
n = n.strip()
n = int(n)
for i in range(n):
    s = input()
    s_dict = {}
    for i in s:
        s_dict[i] = s.count(i)
    s_dict = sorted(s_dict.items(), key=lambda s_dict: s_dict[1], reverse=True)
    num = 0
    for index, i in enumerate(s_dict):
        num += int(i[1]) * (26 - index)
    print(num)