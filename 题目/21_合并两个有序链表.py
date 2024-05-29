# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 21_合并两个有序链表.py
# @Time       ：2023/10/10 19:53
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
将两个升序链表合并为一个新的 升序 链表并返回。
新链表是通过拼接给定的两个链表的所有节点组成的。

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]

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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dumy = ListNode(-1)
        p = dumy
        p1 = l1
        p2 = l2
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
        return dumy.next



if __name__ == '__main__':
    obj = Solution()
    remove_head = obj.mergeTwoLists(ListNode([1, 2, 3, 4, 5]), ListNode([2, 10, 13]))
    cur = remove_head
    while cur:
        print(cur.val)
        cur = cur.next



