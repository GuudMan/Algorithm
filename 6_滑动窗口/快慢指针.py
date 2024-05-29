# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 快慢指针.py
# @Time       ：2024/1/24 15:40
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class NodeList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None

n1 = NodeList(1)
n2 = NodeList(2)
n3 = NodeList(3)
n1.next = n2
n2.next = n3
print(n2.next.val)