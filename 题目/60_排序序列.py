# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 60_排序序列.py
# @Time       ：2023/12/11 19:38
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。


示例 1：
输入：n = 3, k = 3
输出："213"
示例 2：

输入：n = 4, k = 9
输出："2314"
示例 3：

输入：n = 3, k = 1
输出："123"
"""
# ================【功能：】====================
import itertools


class Solution:
    def getPermutation(self, n, k):
        for i, per_list in enumerate(itertools.permutations([i + 1 for i in range(n)])):
            if i == k - 1:
                return ''.join([str(i) for i in per_list])




        # # 存储阶乘
        # factorial_list = [1]
        # for i in range(1, n + 1):
        #     factorial_list.append(factorial_list[-1] * i)
        # print(factorial_list)
        # def func(digits, k):
        #     # 找到数组digits的第k个排列
        #     n = len(digits)
        #     if n == 1:  # 递归条件结束
        #         return str(digits[0])
        #
        #     first_idx, next_k = divmod(k, factorial_list[n - 1])
        #     first = digits.pop(first_idx)
        #     return str(first) + func(digits, next_k)
        # return func(list(range(1, n + 1)), k - 1)




s = Solution()
res = s.getPermutation(3, 2)
print(res)