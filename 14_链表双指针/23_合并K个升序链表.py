# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 23_合并K个升序链表.py
# @Time       ：2024/3/6 11:21
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
"""
# ================【功能：】====================
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
import heapq


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(lst):
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

#
# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         # if len(lists) <= 0: return None
#         # 虚拟头节点
#         dummy = ListNode(-1)
#         p = dummy
#         # 优先级队列， 最小堆
#         pq = []
#         for head in lists:
#             if head:
#                 heapq.heappush(pq, (head.val, id(head), head))
#         print(pq)
#         print('-------')
#         print(heapq)
#         # 将k个链表的头结点加入最小堆
#         while pq:
#             # 获取最小节点， 接到结果链表中
#             node = heapq.heappop(pq)[2]
#             p.next = node
#             if node.next:
#                 heapq.heappush(pq, (node.next.val, id(node.next), node.next))
#             # p指针不断前进
#             p = p.next
#         return dummy.next


class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(-1)
        p = dummy

        # 将其添加到优先队列中
        pq = []
        for head in lists:
            if head:
                heapq.heappush(pq, (head.val, id(head), head))

        # 指向最小的元素
        while pq:
            node = heapq.heappop(pq)[2]
            p.next = node
            # 将node下一个元素push到优先队列中
            if node.next:
                heapq.heappush(pq, (node.next.val, id(node.next), node.next))
            # p指向下一个
            p = p.next
        return dummy.next



# leetcode submit region end(Prohibit modification and deletion)
so = Solution()
lst = [[1, 4, 5], [1, 3, 4], [2, 6]]
linked_lists = [list_to_linked_list(sublist) for sublist in lst]
# print(linked_lists)
res = so.mergeKLists(linked_lists)
while res:
    print(res.val)
    res = res.next
