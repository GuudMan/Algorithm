# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 895_最大频率栈.py
# @Time       ：2024/3/23 14:11
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
实现FreqStack，模拟类似栈的数据结构的操作的一个类。

FreqStack 有两个方法：

1、push(int x)，将整数 x 推入栈中。

2、pop()，它移除并返回栈中出现最频繁的元素；如果最频繁的元素不只一个，则移除并返回最接近栈顶的元素。

示例：

输入：
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
输出：[null,null,null,null,null,null,null,5,7,5,4]
解释：
执行六次 .push 操作后，栈自底向上为 [5,7,5,7,4,5]。然后：

pop() -> 返回 5，因为 5 是出现频率最高的。
栈变成 [5,7,5,7,4]。

pop() -> 返回 7，因为 5 和 7 都是频率最高的，但 7 最接近栈顶。
栈变成 [5,7,5,4]。

pop() -> 返回 5。
栈变成 [5,7,4]。

pop() -> 返回 4。
栈变成 [5,7]。
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
class FreqStack(object):

    def __init__(self):
        # 记录FreqStack中元素的最大频率
        self.maxFreq = 0
        # 记录 FreqStack 中每个 val 对应的出现频率， 后文称为 VF 表
        self.valToFreq = {}
        # 记录频率 freq 对应的 val 列表， 后文称为 FV 表
        self.freqToVals = {}


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # 修改 VF 表， val 对应的 freq 加 1
        freq = self.valToFreq.get(val, 0) + 1
        self.valToFreq[val] = freq
        # 修改 FV 表 在freq对应的列表加 val
        self.freqToVals.setdefault(freq, [])
        self.freqToVals[freq].append(val)
        # 更新 maxFreq
        self.maxFreq = max(self.maxFreq, freq)

    def pop(self, val):
        """
        :rtype: int
        """
        # 修改 FV 表， pop出一个 maxFreq 对应的元素v
        vals = self.freqToVals[self.maxFreq]
        v = vals.pop()
        # 修改 FV 表， v对应的 freq 减 1
        freq = self.valToFreq[v] - 1
        self.valToFreq[v] = freq
        # 更新 maxFreq
        if not vals:
            # 如果 maxFreq 对应的元素空了
            self.maxFreq -= 1
        return v




# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# leetcode submit region end(Prohibit modification and deletion)


















