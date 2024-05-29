# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 61_旋转链表.py
# @Time       ：2023/12/12 18:52
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
"""
# ================【功能：】====================
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        if head is None or head.next is None:
            return head
        len = 1
        temp = head
        while temp.next:
            len += 1
            temp = temp.next
        temp.next = head  # 将链表连接成环链表
        k = k % len
        index = len - k
        while index > 0:
            temp = temp.next
            index -= 1

        newHead = temp.next
        temp.next = None
        return newHead




