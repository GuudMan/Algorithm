# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 移动字符串位置.py
# @Time       ：2023/7/11 19:41
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
def move_char(str_list):
    pos = 0

    for i in range(int(len(str_list))):
        if str_list[i] == '*':
            pos = i
            if pos > 0:
                for j in range(pos, 1, -1):
                    temp = str_list[pos]
                    str_list[pos] = str_list[pos-1]
                    str_list[pos - 1] = temp
                    pos -= 1
    return str_list


def move_char1(str_list):
    j = len(str_list) - 1
    for i in range(len(str_list)-1, -1, -1):
        if str_list[i] != '*':
            str_list[j] = str_list[i]
            j -= 1

    for k in range(j + 1):
        str_list[k] = '*'
    return str_list


if __name__ == '__main__':
    str_list = ["*", '*', 9, '*', 1, '*', 2, '*', '*', '*', 1, 23, '*', 20, 1, 2, '*', '*', "*"]
    res = move_char1(str_list)
    print(res)