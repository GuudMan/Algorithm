# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 填充孔字符串.py
# @Time       ：2023/7/11 20:12
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
def fill_null(str_list):
    for i in range(len(str_list)):
        if str_list[i] == ' ':
            str_list[i] = '%20'
    return str_list


if __name__ == '__main__':
    str_list = [' ', 'a', ' ', 'b', ' ', ' ', 'g']
    res = fill_null(str_list)
    print(res)