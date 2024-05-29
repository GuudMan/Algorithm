# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 反转部分单向链表.py
# @Time       ：2023/8/28 18:53
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个单链表的头指针 head， 以及两个整数 a 和 b，
在单链表中反转 linked_list[a-b] 的结点，然后返回整个链表的头指针。
例如：
单链表[1000, 5, 12, 100, 45, ‘cecil’, 999]，
a = 4， b = 6，
返回的链表是[1000, 5, 12, 100, 999, ‘cecil’, 45]，也就是说，
a 和 b分别为索引值。如果a 和 b 超过了索引范围就返回错误。
"""
# ================【功能：】====================

def list_inversed(list_inver, a, b):
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
    sub_list = list_inver[a: b+ 1]
    sub_list.reverse()
    list_inver[a: b + 1] = sub_list
    return list_inver


if __name__ == '__main__':
    list_inver = [1000, 5, 12, 100, 45, 'cecil', 999]

    res = list_inversed(list_inver, 10, 6)
    print(res)