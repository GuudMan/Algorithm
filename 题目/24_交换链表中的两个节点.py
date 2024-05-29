# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 24_交换链表中的两个节点.py
# @Time       ：2023/10/30 19:37
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个链表，两两交换其中相邻的节点，
并返回交换后链表的头节点。
你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
"""
# ================【功能：】====================
class ListNode():
    def __init__(self, val, next=None):
        if isinstance(val, int):
            self.val = val
            self.next = next
        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            current = self
            for i in range(1, len(val)):
                current.next = ListNode(val[i])
                current = current.next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 如果链表的节点数小于2， 不用交换直接返回
        if not head or not head .next:
            return head
        # 保存链表的下一个节点
        new_head = head.next
        # 交换后面的节点
        head.next = self.swapPairs(new_head.next)
        # 更新节点的指向
        new_head.next = head
        return new_head


s = Solution()
input = ListNode([1, 2, 3, 4])
output = s.swapPairs(input)
print(output)
while output:
    print(output.val)
    output = output.next
