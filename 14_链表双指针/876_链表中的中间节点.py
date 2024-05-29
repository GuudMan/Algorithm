# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 876_链表中的中间节点.py
# @Time       ：2024/3/7 19:24
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个头结点为head 的非空单链表，返回链表的中间结点；如果有两个中间结点，则返回第二个中间结点。

示例 1：

输入：[1,2,3,4,5]
输出：此列表中的结点 3（序列化形式：[3,4,5])
返回的结点值为 3。（测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
示例 2：

输入：[1,2,3,4,5,6]
输出：此列表中的结点 4（序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while fast:
            slow = slow.next
            fast = fast.next.next
        return slow



# leetcode submit region end(Prohibit modification and deletion)
