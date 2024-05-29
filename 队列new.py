# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 队列new.py
# @Time       ：2023/8/30 15:52
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class Node():
    def __init__(self, value, next=0):
        self.value = value
        self.next = next

class Queue():
    def __init__(self, head, data):
        self.head = 0

