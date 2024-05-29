# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 295_数据流中的中位数.py
# @Time       ：2024/3/21 19:01
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

设计一个支持以下两种操作的数据结构：

1、void addNum(int num)从数据流中添加一个整数到数据结构中。

2、double findMedian()返回目前所有元素的中位数。

示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class MedianFinder(object):

    def __init__(self):
        # 小顶堆
        self.large = []
        # 大顶堆
        self.small = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small) >= len(self.large):
            self.small.append(num)
            self.large.append(-heapq.heappushpop(self.small, -self.large[0]))
        else:
            self.large.append(num)
            self.small.append(-heapq.heappushpop(self.large, -self.small[0]))



    def findMedian(self):
        """
        :rtype: float
        """
        # 如果元素不一样多， 多的那个堆的堆顶元素就是中位数
        if len(self.large) < len(self.small):
            return float(self.small[0])
        elif len(self.large) > len(self.small):
            return float(self.large[0])

        # 如果元素一样多， 两个堆顶元素的平均数就是中位数
        return (self.large[0] + self.small[0]) / 2.0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# leetcode submit region end(Prohibit modification and deletion)














