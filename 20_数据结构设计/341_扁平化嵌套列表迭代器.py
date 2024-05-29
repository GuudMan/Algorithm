# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 341_扁平化嵌套列表迭代器.py
# @Time       ：2024/3/23 10:31
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个嵌套的整数列表nestedList。每个元素要么是一个整数，要么是一个列表；该列表的元素也可能是整数或者是其他列表。请你实现一个迭代器将其扁平化，使之能够遍历这个列表中的所有整数。

实现扁平迭代器类NestedIterator：

1、NestedIterator(List<NestedInteger> nestedList)用嵌套列表nestedList初始化迭代器。

2、int next()返回嵌套列表的下一个整数。

3、boolean hasNext()如果仍然存在待迭代的整数，返回true；否则，返回false。

你的代码将会用下述伪代码检测：

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
如果res与预期的扁平化列表匹配，那么你的代码将会被判为正确。
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from collections import deque


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # 不直接用 nestedList 的引用， 是因为不能确定它的底层实现
        # 必须保证是 LinkedList， 否则下面的 oddFirst 会很低效
        self.list = deque(nestedList)


    def next(self):
        """
        :rtype: int
        """
        # hasNext方法保证了第一个元素一定是整数类型
        return self.list.popleft().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        # 循环拆分列表元素， 直到列表第一个元素是整数类型
        while self.list and not self.list[0].isInteger():
            # 当列表开头第一个元素是列表类型时， 进入循环
            first = self.list.popleft().getList()
            # 将第一个列表打平并按照顺序添加到开头
            for i in range(len(first) - 1, -1, -1):
                self.list.appendleft(first[i])
        return bool(self.list)



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# leetcode submit region end(Prohibit modification and deletion)
