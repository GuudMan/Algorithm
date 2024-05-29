# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 判断一个链表是否是回文结构.py
# @Time       ：2023/8/28 18:45
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
判断一个链表是否是回文结构，如果是返回 True，否则返回 False
比如，给出一个链表为[2, 5, 12, 198, 12, 5, 2]，返回 True，
给定链表[2, 5, 12, 198, 12, 54, 20]，返回 False。
"""
# ================【功能：】====================

def huiwenshu(data_list):
    '''
    给定一个括号字符串 str，返回最长的有效括号字符串
    方法：动态规划求解，做到时间复杂度 o(n)，空间复杂度 o(n)。创建一个与字符串同等长度的数组 dp[]，
        其含义是对应 str[i]结尾的字符串的最长有效子串的长度。然后即可开始求解。
    :param str: 给定的括号字符串
    :return: 最长有效子串
    '''
    if len(data_list) < 1:
        return False
    if len(data_list) % 2 == 0:
        return False
    middle_index = len(data_list) % 2
    len_list = len(data_list)
    for i in range(middle_index):
        if data_list[i] != data_list[len_list - 1 - i]:
            return False
    return True


if __name__ == '__main__':
    list_data = [2, 1, 2]
    res = huiwenshu(list_data)
    print(res)