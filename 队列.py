# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 队列.py
# @Time       ：2023/8/28 19:12
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class Node(object):
    def __init__(self, value, next=0):
        self.value = value
        self.next = next

class Queue(object):
    "由于python操作地址困难，这里给出了链队列的数据结构"
    "队列中存在两个指针，一个头指针，一个尾指针，但在这里省去了，只留了一个尾指针"
    def __init__(self):
        self.head = 0
    def init_queue(self, data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            p.next = Node(i)
            p = p.next
    def clear_queue(self):
        self.head = 0

    def is_empyt(self):
        if self.head == 0:
            return True
        else:
            return False

    def get_length(self):
        p, length = self.head, 0
        while p.next != 0:
            length += 1
            p = p.next
        return length

    def en_queue(self, value):
        if self.is_empyt():
            self.head = Node(value)
        else:
            p = self.head
            for _ in range(self.get_length()):
                p = p.next
            p.next = Node(value)

    def get_head(self):
        if self.is_empyt():
            print("This is an empty queue")
        else:
            return self.head.value

    def de_queue(self):
        if self.is_empyt():
            print("This is an empty queue")
            return
        else:
            p = self.head
            self.head = p.next
            return p.value

    def show_queue(self):
        if self.is_empyt():
            print("This is an empty queue")
        else:
            p, container = self.head, []
            for _ in range(self.get_length()):
                container.append(p.value)
                p = p.next
            container.append(p.value)
            print(container)


q = Queue()
q.init_queue([1, 7, 22, 45, 2, 4, 5, 654])
q.show_queue()
q.en_queue(999)
q.show_queue()
print(q.get_head())
q.de_queue()
q.show_queue()
q.de_queue()
q.show_queue()

