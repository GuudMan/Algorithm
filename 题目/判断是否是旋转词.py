# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 判断是否是旋转词.py
# @Time       ：2023/7/18 19:30
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
如果将一个 str1 从任意的位置切分开，分成两部分，将后面一部分放置在前面， 再组合起来成为 str2，构成了旋转词。
例如：str1 = “apple”，str2 = “leapp”，两个词就是旋转词。
"""
# ================【功能：】====================


def is_rotation(strs1, strs2):
    if strs1 == "" or strs2 == "" or len(strs1) != len(strs2):
        return False
    str_double = strs1 + strs1
    if strs2 in str_double:
        return True
    else:
        return False


if __name__ == '__main__':
    strs1 = "apple"
    strs2 = "leapp"
    res = is_rotation(strs1, strs2)
    print(res)
