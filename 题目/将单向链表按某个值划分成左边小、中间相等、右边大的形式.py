# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 将单向链表按某个值划分成左边小、中间相等、右边大的形式.py
# @Time       ：2023/8/21 19:35
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个单向链表，如 LinkedList [21, 5, 120, 19, 72, 50, 312]。
再给定任意一个数值，比如50，返回一个链表，保证左边小、中间相等、右边大的形式，
比如该例子的返回链表结果为：[21, 5, 19, 50, 120, 72, 312]
再比如给定值100，返回的链表结果为：[21, 5, 19, 72, 50, 120, 312]
且需要保证修改后的链表中，不论是左、中、右哪一部分结点的先后顺序和原链表中一致。
"""


# ================【功能：】====================



def linklist_sort(list_data, num):
    '''
    给定一个括号字符串 str，返回最长的有效括号字符串
    方法：动态规划求解，做到时间复杂度 o(n)，空间复杂度 o(n)。创建一个与字符串同等长度的数组 dp[]，
        其含义是对应 str[i]结尾的字符串的最长有效子串的长度。然后即可开始求解。
    :param str: 给定的括号字符串
    :return: 最长有效子串
    '''
    small_list = []
    big_list = []
    for i in list_data:
        if i < num:
            small_list.append(i)
        if i > num:
            big_list.append(i)

    if num not in list_data:
        res = small_list + big_list
    else:
        res = small_list + [num] + big_list
    return res


if __name__ == '__main__':
    list_data = [21, 5, 120, 19, 72, 50, 312]
    num = 43255
    res = linklist_sort(list_data, num)
    print(res)
