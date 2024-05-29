# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 460_LFU缓存.py
# @Time       ：2024/3/23 9:22
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
请你为最不经常使用缓存算法（LFU） 设计并实现数据结构。

实现LFUCache类：

1、LFUCache(int capacity)用数据结构的容量 capacity初始化对象。

2、int get(int key)如果键存在于缓存中，则获取键的值，否则返回 -1。

3、void put(int key, int value)如果键已存在，则变更其值；如果键不存在，插入键值对。当缓存达到其容量时，则应该在插入新键值对之前，删除最不经常使用的键值对；若存在两个或更多个键具有相同使用频率时，应该去除最近最久未使用的键。

注：「键值对的使用次数」就是自插入该键以来对其调用get和put函数的次数之和，使用次数会在对应键被移除后置为 0。

示例：

输入：
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
输出：
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

解释：
// cnt(x) = 键 x 的使用计数
// cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的）
LFUCache lFUCache = new LFUCache(2);
lFUCache.put(1, 1);   // cache=[1,_], cnt(1)=1
lFUCache.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lFUCache.get(1);      // 返回 1
                      // cache=[1,2], cnt(2)=1, cnt(1)=2
lFUCache.put(3, 3);   // 去除键 2，因为 cnt(2)=1，使用计数最小
                      // cache=[3,1], cnt(3)=1, cnt(1)=2
lFUCache.get(2);      // 返回 -1（未找到）
lFUCache.get(3);      // 返回 3
                      // cache=[3,1], cnt(3)=2, cnt(1)=2
lFUCache.put(4, 4);   // 去除键 1，1 和 3 的 cnt 相同，但 1 最久未使用
                      // cache=[4,3], cnt(4)=1, cnt(3)=2
lFUCache.get(1);      // 返回 -1（未找到）
lFUCache.get(3);      // 返回 3
                      // cache=[3,4], cnt(4)=1, cnt(3)=3
lFUCache.get(4);      // 返回 4
                      // cache=[3,4], cnt(4)=2, cnt(3)=3

"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # key到val的映射， 后文称为KV表
        self.keyToVal = {}
        # key到freq的映射， 后文称为KF表
        self.keyToFreq = {}
        # freq到key列表的映射， 后文称为FK表
        self.freqToKeys = {}
        # 记录最小的频次
        self.minFreq = 0
        # 记录LFU缓存的最大容量
        self.cap = capacity



    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keyToVal:
            return -1
        # 增加key对应的freq
        self._increaseFreq(key)
        return self.keyToVal[key]


    def put(self, key, val):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.cap <= 0:
            return
        # 若key已存在， 修改对应的val即可
        if key in self.keyToVal:
            self.keyToVal[key] = val
            # key对应的freq加1
            self._increaseFreq(key)
        # key不存在， 需要插入
        # 容量已满的话需要淘汰一个freq最小的key
        if self.cap <= len(self.keyToVal):
            self._removeMinFreq()

        # 插入key和val， 对应的freq为1
        # 插入kv表
        self.keyToVal[key] = val
        # 插入kF表
        self.keyToFreq[key] = 1
        # 插入KF表
        self.freqToKeys.setdefault(1, set())
        self.freqToKeys[1].add(key)
        # 插入新key后最小的freq肯定是1
        self.minFreq = 1

    def _increaseFreq(self, key):
        freq = self.keyToFreq[key]
        # 更新kf表
        self.keyToFreq[key] = freq + 1
        # 更新KF表
        # 将key从freq对应的列表中删除
        self.freqToKeys[freq].remove(key)
        # 将key加入freq + 1对应的列表中
        self.freqToKeys.setdefault(freq + 1, set())
        self.freqToKeys[freq + 1].add(key)
        # 如果freq对应的列表空了， 移除这个freq
        if not self.freqToKeys[freq]:
            del self.freqToKeys[freq]
            # 如果这个freq恰好是minFreq， 更新minFreq
            if freq == self.minFreq:
                self.minFreq += 1

    def _removeMinFreq(self):
        # freq最小的key列表
        keyList = self.freqToKeys[self.minFreq]
        # 其中最先被插入的那个key， 就是该被淘汰的key
        deleteKey = keyList.pop()
        # 更新 FK 表
        if not keyList:
            del self.freqToKeys[self.minFreq]
        # 更新KV表
        del self.keyToVal[deleteKey]
        # 更新 KF 表
        del self.keyToFreq[deleteKey]






# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
