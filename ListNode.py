# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : ListNode.py
# @Time       ：2023/11/13 19:55
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class ListNode3():
    def __init__(self, val, next=None):
        if isinstance(val, int):
            self.val = val
            self.next = next
            current = self
        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            current = self
            for i in range(1, len(val)):
                current.next = ListNode(val[i])
                current = current.next

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class ListNode():
    def __init__(self, head=None):
        self.head = head

# node1 = Node(1)
# node2 = Node(2)
# node1.next = node2
# listNode = ListNode()
# listNode.head = node1
#
# print(listNode.head.next.val)



class ListNode2():
    def __init__(self, val, next=None):
        if not isinstance(val, list):
            self.val = val
            self.next = None
            current = self
        if isinstance(val, list):
            self.val = val[0]
            self.next = None
            current = self
            for i in range(1, len(val)):
                current.next = ListNode2(val[i])
                current = current.next


listNode2 = ListNode3([1, 2, 3, 4])
while listNode2.next:
    print(listNode2.val)
    # listNode2.next

