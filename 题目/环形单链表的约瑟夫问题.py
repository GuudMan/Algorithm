# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 环形单链表的约瑟夫问题.py
# @Time       ：2023/8/24 20:03
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
一个环形单链表，从头结点开始向后，指针每移动一个结点，就计数加1，
当数到第m个节点时，就把该结点删除，然后继续从下一个节点开始从1计数，
循环往复，直到环形单链表中只剩下了一个结点，返回该结点。
"""
# ================【功能：】====================


def link_circle(list_data, num):
    '''
    给定一个括号字符串 str，返回最长的有效括号字符串
    方法：动态规划求解，做到时间复杂度 o(n)，空间复杂度 o(n)。创建一个与字符串同等长度的数组 dp[]，
        其含义是对应 str[i]结尾的字符串的最长有效子串的长度。然后即可开始求解。
    :param str: 给定的括号字符串
    :return: 最长有效子串
    '''
    i = 0
    len_num = len(list_data)
    while len(list_data) > 1:
        print(num)
        num = (num + i) % len_num
        print('--------')
        print(num)
        list_data.pop(num)
        i += 1
        print(list_data)
        len_num = len(list_data)
        if len_num == 1:
            return list_data[0]


if __name__ == '__main__':
    list_data = [21, 5, 120, 19, 72, 50, 312]
    num = 4
    res = link_circle(list_data, num)
    print(res)
