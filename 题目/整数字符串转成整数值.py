# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 整数字符串转成整数值.py
# @Time       ：2023/7/13 12:15
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个字符串，如果其中所有的字符都是数字，且符合人们日常的书写规范，则返回该整数值，否则返回0。
例如：“123”，返回123；
“038123”，返回0；
“dfa423”，返回0；
“-482”，返回-482；
“-03”，返回0。
"""


# ================【功能：】====================
def num_conv(strs):
    if strs == "":
        return 0
    char_list = list(strs)
    if char_list[0] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '-']:
        return 0
    else:
        if char_list[0] == '-' and char_list[1] == '0':
            return 0
        else:
            return int(strs)


if __name__ == '__main__':
    num_str = "0.23424"
    res = num_conv(num_str)
    print(res)

    print(ord('9'))

