# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 计算字符串中所有数字之和.py
# @Time       ：2023/7/18 20:01
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个字符串，计算其中所有数字的和。其中，不考虑小数点，如果有奇数个“-”号，则数字为负，偶数个则数字为正。
例如，“a12b3mnh4”, 返回值19，
“-2fds—-43fnd”，返回值41。
"""
# ================【功能：】====================

def strs_sum(strs):
    if strs == "":
        return False
    sum, num, pos = 0, 0, 1
    for i in range(0, len(strs)):
        if 48 <= ord(strs[i]) <= 57:
            num = num * 10 + int(strs[i]) * pos
        else:  # 非字符
            sum += num
            num = 0
            if strs[i] == '-':
                if i - 1 > -1 and strs[i - 1] == '-':
                    pos = pos
                else:
                    pos = -1
            else:
                pos = 1

    return sum


if __name__ == '__main__':
    strs = "2fds—-43fnd"
    res = strs_sum(strs)
    print(res)