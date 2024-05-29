# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 19_删除链表的倒数第N个节点.py
# @Time       ：2024/3/5 20:20
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        x = self.findFromEnd(head, n + 1)
        x.next = x.next.next
        return dummy.next

    def findFromEnd(self, head, k):
        p1 = head
        for i in range(k):
            p1 = p1.next
        p2 = head
        while p1:
            p2 = p2.next
            p1 = p1.next
        return p2






# leetcode submit region end(Prohibit modification and deletion)
