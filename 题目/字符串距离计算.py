# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 字符串距离计算.py
# @Time       ：2023/7/10 19:10
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""


# ================【功能：】====================

def distance_str(str_list, a, b):
    if a not in str_list or b not in str_list:
        return -1
    elif a == b:
        return 0
    else:
        a_index = []
        b_index = []
        for i in range(len(str_list)):
            if str_list[i] == b:
                b_index.append(i)
            if str_list[i] == a:
                a_index.append(i)
        res = []
        for a_i in a_index:
            for b_i in b_index:
                res.append(abs(a_i - b_i))
        return min(res)


def distance_str_1(strs, str1, str2):
    if str1 not in strs or str2 not in strs:
        return -1
    elif str1 == str2:
        return 0
    else:
        pos1, pos2 = 0, len(strs)
        dis, min =1, len(strs)
        for i in range(len(strs)):
            if strs[i] == str1:
                pos1 = i
                for j in range(0, len(strs)):
                    if strs[j] == str2:
                        pos2 = j
                dis = abs(pos2 - pos1)
                if dis < min:
                    min = dis
    return min


if __name__ == '__main__':
    str_list = ['*', '3', '*', '5', '10', '9', '7', '1', '*']
    a = '*'
    b = '3'
    # dis = distance_str(str_list, a, b)
    dis = distance_str_1(str_list, a, b)
    print(dis)
