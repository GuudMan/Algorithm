# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 23_合并K个升序链表.py
# @Time       ：2023/10/17 19:37
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
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

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]

"""


# ================【功能：】====================

class ListNode():
    def __init__(self, val, next=None):
        if isinstance(val, int):
            self.val = val
            self.next = next
        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            current = self
            for i in range(1, len(val)):
                current.next = ListNode(val[i])
                current = current.next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:

        def mergeKlist(self, lists):
            self._lists = lists
            return self.merge(0, len(lists) - 1)


        def merge(self, left, right):
            if left == right:
                return left._lists[left]
            if left > right:
                return None
            middle = (left + right) // 2
            return self.mergeTwoList(self.merge(left, middle), self.merge(middle + 1, right))


        def mergeTwoList(self, a, b):
            merge = ListNode(-1)
            head = merge
            while a and b:
                if a.val > b.val:
                    head.next = b
                    b = b.next
                else:
                    head.next = a
                    a = a.next
                head = head.next
            head.next = a if a else b
            return merge.next


lists = [[7, 4, 5], [1, 3, 4], [2, 6]]
l_nodes = []
for l in lists:
    listnode = ListNode(l)
    l_nodes.append(listnode)

solution = Solution()
merge = solution.mergeKLists(l_nodes)
while merge:
    print(merge.val)
    merge = merge.next
