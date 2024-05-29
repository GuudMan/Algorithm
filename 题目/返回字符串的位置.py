# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 返回字符串的位置.py
# @Time       ：2023/7/13 11:26
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""


# ================【功能：】====================
def find_char(str, ch):
    if ch not in str:
        return -1
    if ch is None:
        return -1
    res = []
    for i in str:
        if i == ch:
            res.append(str.index(i))
    return min(res)


def find_char1(strs, ch):
    if ch not in strs:
        return -1
    if ch is None:
        return -1
    left = 0
    right = len(strs) - 1
    while left < right:
        mid = int((left + right) / 2)
        if strs[mid] == None:
            i = mid - 1
            while 0 < i < mid:
                if strs[i] > ch:
                    i -= 1
                    if strs[i] == ch:
                        return i
                else:
                    break

        elif strs[mid] > ch:
            right = mid
        elif strs[mid] < ch:
            left = mid
        elif strs[mid] == ch:
            return mid
        else:
            return -1


if __name__ == '__main__':
    strs = ['a', None, 'b', None, 'd', 'd', None, 'k', 'm']
    ch = 'k'
    res = find_char(strs, ch)
    print(res)
