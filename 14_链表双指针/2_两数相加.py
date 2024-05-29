# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 2_两数相加.py
# @Time       ：2024/3/5 19:54
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
"""


# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        dummy = ListNode(-1)
        p = dummy
        carry = 0
        while p1 or p2 or carry > 0:
            val = carry
            if p1:
                val += p1.val
                p1 = p1.next
            if p2:
                val += p2.val
                p2 = p2.next
            # 处理进位情况
            carry = val / 10
            val = val % 10
            p.next = ListNode(val)
            p = p.next
        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)
so = Solution()
l1 = [2, 4, 3]
l11 = ListNode(l1[0])
l11.next = ListNode(l1[1])
l11.next.next = ListNode(l1[2])

l2 = [5, 6, 4]
l21 = ListNode(l2[0])
l21.next = ListNode(l2[1])
l21.next.next = ListNode(l2[2])
res = so.addTwoNumbers(l11, l21)
while res:
    print(res.val)
    res = res.next
