# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 判断字符串是否只出现过一次.py
# @Time       ：2023/7/13 11:55
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
def if_ones(strs):
    set_a = set(strs)
    if len(strs) == len(set_a):
        return True
    else:
        return False

if __name__ == '__main__':
    strs = ['a', 'b', 'c', 'c']
    res = if_ones(strs)
    print(res)