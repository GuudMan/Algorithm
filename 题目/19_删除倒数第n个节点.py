# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 19_删除倒数第n个节点.py
# @Time       ：2023/10/9 19:49
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]


提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""
# ================【功能：】====================
class ListNode:
    #定义链表类
    def __init__(self,val,next=None):
        if isinstance(val,int):
            self.val = val
            self.next = next
        elif isinstance(val,list):
            self.val = val[0]
            self.next = None
            current = self
            for i in range(1,len(val)):
                current.next = ListNode(val[i])
                current = current.next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def findFromEnd(head, k):
            print('---')
            print(k)
            print('----')
            p1 = head
            for i in range(k):
                p1 = p1.next
            p2 = head
            while p1 != None:
                p1 = p1.next
                p2 = p2.next
            return p2

        # 创造一个哑结点
        dumy = ListNode(-1)
        dumy.next = head
        # 倒数第n个，要找到倒数第n+1个节点
        x = findFromEnd(head, n+1)
        x.next = x.next.next
        return dumy.next


if __name__ == '__main__':
    obj = Solution()
    remove_head = obj.removeNthFromEnd(ListNode([1, 2, 3, 4, 5]), 3)
    cur = remove_head
    while cur:
        print(cur.val)
        cur = cur.next