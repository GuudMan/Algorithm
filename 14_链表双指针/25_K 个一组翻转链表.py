# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 25_K 个一组翻转链表.py
# @Time       ：2024/3/7 19:32
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个链表，请你对每 k 个节点一组进行翻转，返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度，如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return None
        a = head
        b = head
        for i in range(k):
            if not b:
                # 不足k个， 不需要反转
                return head
            b = b.next
        # 反转前k个元素
        newHead = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead

    def reverse(self, a, b):
        pre = ListNode(-1)
        cur = a
        nxt = a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

# leetcode submit region end(Prohibit modification and deletion)





