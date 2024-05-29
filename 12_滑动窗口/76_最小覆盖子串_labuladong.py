# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 76_最小覆盖子串.py
# @Time       ：2024/2/28 9:33
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个字符串s、一个字符串t，返回s中涵盖t所有字符的最小子串；如果s中不存在涵盖t所有字符的子串，则返回空字符串""。
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。

"""
# ================【功能：】====================
class Solution:
    def minWindow(self, s: str, t: str):
        from collections import Counter
        left = 0
        tt = Counter(t)
        res = {}
        for si in s:
            if si in tt:
               res[si] += 1
        print(res)


so = Solution()
s = "ADOBECODEBANC"
t = "ABC"
res = so.minWindow(s, t)
print(res)

# 伪代码
"""
res = infinity  # 初始结果为无穷大
l, r = 0, 0   # s中包含T中所有字符最小子串的左右边界
for ch in s:
    # 右指针右移
    if T 包含字符ch：
        将ch添加到char中
        将ch对应的索引添加到idx中
    # 左指针右移， 以寻找当前子串中包含T串所有字符的最小子串
    while char != "" AND char中包含T中所有的字符:
        取出idx[0]和idx[-1]  # 取出idx中第一个和最后一个值
        if 根据两个索引计算出的串场 < res:
            l, r = idx[0], idx[-1]
            res = r - l + 1
        char串移出第一个字符
        idx索引列表移出对应的索引值
        
        
    
"""








