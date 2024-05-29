# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : func.py
# @Time       ：2024/3/6 14:23
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(lst):
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

lst = [[1,4,5],[1,3,4],[2,6]]
linked_lists = [list_to_linked_list(sublist) for sublist in lst]

for i, head in enumerate(linked_lists):
    print(f"Linked List {i+1}:")
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next
    print()
