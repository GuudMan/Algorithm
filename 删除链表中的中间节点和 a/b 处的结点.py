# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : b 处的结点.py
# @Time       ：2023/8/29 19:02
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个链表的头结点 head，实现删除链表中的中间节点的函数。
例如：给定链表[1, 5, 12, 33, 45, 171, 999, 1001, 2000]，删除结点 45，
给定链表[1, 5, 12, 33, 45, 171, 999, 1001]，删除结点 33。
如果链表为空或长度为1，则不删除任何结点。
"""
# ================【功能：】====================

def list_delete(list_inver, a, b):
    if len(list_inver) < 1:
        return False
    if a not in range(len(list_inver)):
        return False
    if b not in range(len(list_inver)):
        return False
    if a > b:
        temp = a
        a = b
        b = temp
    sub_list = list_inver[a: b + 1]
    sub_list.reverse()
    list_inver[a: b + 1] = sub_list
    return list_inver


if __name__ == '__main__':
    list_inver = [1000, 5, 12, 100, 45, 1, 999]

    res = list_delete(list_inver, 10, 6)
    print(res)
