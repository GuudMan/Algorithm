# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 25_k个一组翻转链表.py
# @Time       ：2023/10/30 19:23
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
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
    def reverseKGroup(self, head, k: int):
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count:
                temp = head.next
                head.next = cur
                cur = head
                head = temp
                count -= 1
            head = cur
        return head



input =  ListNode([1,2,3,4,5])
s = Solution()
# (s.reverseKGroup(input, 2))

out = s.reverseKGroup(input, 2)
while out:
    print(out.val)
    out = out.next