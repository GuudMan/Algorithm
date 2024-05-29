# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 232_用栈实现队列.py
# @Time       ：2024/3/18 17:01
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
实现MyQueue类：
1、void push(int x)将元素 x 推到队列的末尾

2、int pop()从队列的开头移除并返回元素

3、int peek()返回队列开头的元素

4、boolean empty()如果队列为空，返回true；否则，返回false
"""
# ================【功能：】====================
# leetcode submit region begin(Prohibit modification and deletion)


class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        # 先调用peek保证s2非空
        self.peek()
        return self.s2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.s2:
            # 把s1元素压入s2
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.s1 and not self.s2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# leetcode submit region end(Prohibit modification and deletion)
