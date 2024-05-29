# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 23_合并 K 个升序链表.py
# @Time       ：2024/3/19 19:21
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：

"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
import heapq


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        # 虚拟头结点
        dummy = ListNode(-1)
        p = dummy
        # 优先级队列， 最小堆
        pq = []
        for head in lists:
            if head:
                heapq.heappush(pq, (head.val, id(head), head))
        # 将k个链表的头结点加入最小堆
        while pq:
            node = heapq.heappop(pq)[2]
            p.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val, id(node.next), node.next))
            # p 指针不断前进
            p = p.next
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)








