# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 141_环形链表.py
# @Time       ：2024/3/6 17:15
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个链表，判断链表中是否有环，如果链表中存在环，则返回true，否则返回false。
输入：head = [3,2,0,-4], pos = 1
输出：true
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
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# leetcode submit region end(Prohibit modification and deletion)
