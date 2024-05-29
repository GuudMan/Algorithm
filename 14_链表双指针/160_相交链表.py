# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 160_相交链表.py
# @Time       ：2024/3/6 17:55
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你两个单链表的头节点 headA和headB，请你找出并返回两个单链表相交的起始节点。
如果两个链表没有交点，返回null。

题目数据保证整个链式结构中不存在环，算法不能修改链表的原始结构。
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8（注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB

            if p2:
                p2 = p2.next
            else:
                p2 = headA
        return p1




# leetcode submit region end(Prohibit modification and deletion)






