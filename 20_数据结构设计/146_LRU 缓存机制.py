# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 146_LRU 缓存机制.py
# @Time       ：2024/3/21 19:26
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
运用你所掌握的数据结构，设计和实现一个 LRU（最近最少使用）缓存机制。

实现LRUCache类：

1、LRUCache(int capacity)以正整数作为容量 capacity初始化 LRU 缓存。

2、int get(int key)如果关键字key存在于缓存中，则返回关键字的值，否则返回-1。

3、void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该键值对。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1（未找到）
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1（未找到）
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
import collections


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = collections.OrderedDict()


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        # 将key变为最近使用
        self.cache.move_to_end(key)
        return self.cache[key]


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            # 修改key的值
            self.cache[key] = value
            # 将key变为最近使用
            self.cache.move_to_end(key)
            return
        if len(self.cache) >= self.cap:
            # 链表头部就是最久未使用的key
            self.cache.popitem(last=False)
        # 将新的key添加到链表尾部
        self.cache[key] = value




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
