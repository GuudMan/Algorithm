# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 链表.py
# @Time       ：2023/10/9 19:57
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""


# ================【功能：】====================
class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class ListNode(object):
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    listNode = ListNode()
    node1 = Node(1)
    node2 = Node(2)

    listNode.head = node1
    node1.next = node2

    print(listNode.head.item)
    print(listNode.head.next.item)
