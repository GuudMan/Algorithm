# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 225_用队列实现栈.py
# @Time       ：2024/3/18 17:15
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop和empty）。

实现MyStack类：

1、void push(int x)将元素 x 压入栈顶。

2、int pop()移除并返回栈顶元素。

3、int top()返回栈顶元素。

4、boolean empty()如果栈是空的，返回true；否则，返回false。
"""
# ================【功能：】====================
from queue import Queue

# leetcode submit region begin(Prohibit modification and deletion)
class MyStack(object):
    def __init__(self):
        self.q = Queue()
        self.top_elem = 0


    def push(self, x):
        """
        :type x: int
        :rtype: None
        添加元素到栈顶
        """
        # x 是队列的队尾，是栈的栈顶
        self.q.put(x)
        self.top_elem = x


    def pop(self):
        """
        :rtype: int
        # 删除栈顶元素并返回
        """
        size = self.q.qsize()
        # 留下队尾2个元素
        while size > 2:
            self.q.put(self.q.get())
            size -= 1
        # 记录新的队尾元素
        self.top_elem = self.q.queue[0]
        self.q.put(self.q.get())
        # 删除之前的队尾元素
        return self.q.get()


    def top(self):
        """
        :rtype: int
        # 返回栈顶元素
        """
        return self.top_elem


    def empty(self):
        """
        :rtype: bool
        # 判断栈是否为空
        """
        return self.q.empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# leetcode submit region end(Prohibit modification and deletion)
