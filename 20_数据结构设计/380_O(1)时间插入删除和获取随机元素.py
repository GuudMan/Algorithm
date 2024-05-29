# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 380_O(1)时间插入删除和获取随机元素.py
# @Time       ：2024/3/23 9:55
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
实现RandomizedSet类：

1、RandomizedSet()初始化RandomizedSet对象

2、bool insert(int val)当元素val不存在时，向集合中插入该项，并返回true；否则，返回false。

3、bool remove(int val)当元素val存在时，从集合中移除该项，并返回true；否则，返回false。

4、int getRandom()随机返回现有集合中的一项，每个元素应该有相同的概率被返回。

你必须实现类的所有函数，并满足每个函数的平均时间复杂度为O(1)。

示例：

输入：
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
输出：
[null, true, false, true, 2, true, false, 2]

解释：
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // 向集合中插入 1。返回 true 表示 1 被成功地插入。
randomizedSet.remove(2); // 返回 false，表示集合中不存在 2。
randomizedSet.insert(2); // 向集合中插入 2。返回 true。集合现在包含 [1,2]。
randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2。
randomizedSet.remove(1); // 从集合中移除 1，返回 true。集合现在包含 [2]。
randomizedSet.insert(2); // 2 已在集合中，所以返回 false。
randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2。
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
import random

import mkl_random


class RandomizedSet(object):

    def __init__(self):
        self.nums = []  # 存储元素的值
        self.valToIndex = dict()  # 记录每个元素对应在nums中的索引


    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # 若 val 已存在， 不用再插入
        if val in self.valToIndex:
            return False
        # 若 val 不存在， 插入到 nums 尾部
        # 并记录 val 对应的索引值
        self.valToIndex[val] = len(self.nums)
        self.nums.append(val)
        return True


    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # 若 val 不存在， 不用删除
        if val not in self.valToIndex:
            return False
        # 先拿到 val 的索引
        index = self.valToIndex[val]
        # 将最后一个元素对应的索引修改为 index
        self.valToIndex[self.nums[-1]] = index
        # 交换 val 和最后一个元素
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        # 在数据中删除元素 val
        self.nums.pop()
        # 删除元素 val 对应的索引
        del self.valToIndex[val]
        return True



    def getRandom(self):
        """
        :rtype: int
        """
        # 随机获取 nums 中的一个元素
        return self.nums[random.randint(0, len(self.nums) - 1)]




# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# leetcode submit region end(Prohibit modification and deletion)
