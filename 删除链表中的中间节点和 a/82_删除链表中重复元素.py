# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 82_删除链表中重复元素.py
# @Time       ：2023/12/21 19:44
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
        def deleteDuplicates(self, head):
                """
                :type head: ListNode
                :rtype: ListNode
                """
                temp = head
                while temp:
                        if temp.val == temp.next.val:
                                head = head.next
                                temp = temp.next
                return head

# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
res = s.deleteDuplicates(ListNode([1, 2, 2, 3, 3, 4]))
