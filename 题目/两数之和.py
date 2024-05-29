# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 两数之和.py
# @Time       ：2023/9/7 18:35
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

"""


# ================【功能：】====================
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def show(self):
        print(self.val)
        while self.next is not None:
            print(self.next.val)
            self.next = self.next.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if l1 is None and l2 is None:
        #     return None
        # if l1 is None:
        #     return l2
        # if l2 is None:
        #     return l1
        #
        # # 设置初始的进位
        # flag = 0
        # res = ListNode(0)
        # # l1或l22不为空，就继续
        # while l1 or l2:
        #     sum = 0
        #     if l1:  # l1不为空，将该节点的值赋值给sum
        #         sum += l1.val
        #         l1 = l1.next
        #     if l2:
        #         sum += l2.val
        #         l2 = l2.next
        #     # 计算个位数
        #     sum_ge = (sum + flag) % 10
        #     # 进位
        #     flag = (sum + flag) // 10
        #     res.next = ListNode(sum_ge)
        #     res = res.next
        # return res
        # 如果有一个链表为空，返回另外一个

        # sum = 0
        # res = temp = ListNode(0)
        # while l1 or l2 or sum:
        #     if l1:
        #         sum += l1.val
        #         l1 = l1.next
        #     if l2:
        #         sum += l2.val
        #         l2 = l2.next
        #     # 余数 其实就是个位和
        #     val = sum % 10
        #     # 进位
        #     sum = sum // 10
        #     temp.next = temp = ListNode(val)
        #     # temp.next = temp
        #     # res = ListNode(val)
        #     # res.next = res
        #
        # return res.next
        if l1 and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # 设置进位
        carry = 0
        # 某个节点的和
        sum = 0
        # 设置虚拟头节点
        temp = ListNode(0)
        # 指针p负责构建新链表
        p = temp
        while l1 or l2 or carry > 0:

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # 个位
            ge = (sum + carry) % 10
            carry = (sum + carry) // 10
            print("carry", carry)
            sum = carry

            # 构建新节点
            p.next = ListNode(ge)
            p = p.next
        return temp.next


if __name__ == '__main__':
    s = Solution()
    # 9,9,9,9,9,9,9
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l1.next.next.next = ListNode(9)
    l1.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next.next = ListNode(9)

    l2 = ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    l2.next.next.next = ListNode(9)
    res = s.addTwoNumbers(l1, l2)
    print(res.show())
    # print(l2.show())
