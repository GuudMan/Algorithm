# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 获取字符串的统计字符串.py
# @Time       ：2023/7/13 12:03
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
def ch_count(strs):
    dict_strs = {}
    res = ""
    for i in strs:
        dict_strs[i] = dict_strs[i] + 1 if i in dict_strs.keys() else 1

    for key, value in dict_strs.items():
        res += str(key) + "_" + str(value)
        res += '_'

    res = res[:-1]
    return res


if __name__ == '__main__':
    strs = "fffjkk999234234599022____"
    res = ch_count(strs)
    print(res)
