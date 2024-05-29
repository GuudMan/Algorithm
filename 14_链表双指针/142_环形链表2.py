# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 142_环形链表2.py
# @Time       ：2024/3/6 17:31
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个链表，返回链表开始入环的第一个节点，如果链表无环，则返回 null（不允许修改给定的链表）。
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            # fast指针遇到空指针说明没有环
            return None

        # 重新指向头结点
        slow = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow
# leetcode submit region end(Prohibit modification and deletion)







