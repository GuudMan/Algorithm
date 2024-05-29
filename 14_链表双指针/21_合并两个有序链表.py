# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 21_合并两个有序链表.py
# @Time       ：2024/3/5 20:34
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
"""


# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p1 = list1
        p2 = list2
        dummy = ListNode(-1)
        p = dummy
        res = []
        while p1 and p2:
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next

        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
