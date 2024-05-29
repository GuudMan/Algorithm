# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 234_回文链表.py
# @Time       ：2024/3/9 15:13
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个单链表的头节点head，请你判断该链表是否为回文链表。如果是，返回true；否则返回false。
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        left = head
        right = self.reverse(slow)
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return cur







# leetcode submit region end(Prohibit modification and deletion)
