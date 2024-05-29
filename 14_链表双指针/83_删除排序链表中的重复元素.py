# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 83_删除排序链表中的重复元素.py
# @Time       ：2024/3/9 9:58
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        pre = head
        slow = head
        fast = head
        while fast:
            if slow.val == fast.val:
                fast = fast.next
            else:
                slow.next = fast
                fast = fast.next
                slow = slow.next
        slow.next = None
        return pre



# leetcode submit region end(Prohibit modification and deletion)
