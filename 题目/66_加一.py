# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 66_加一.py
# @Time       ：2023/12/14 18:28
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
"""
# ================【功能：】====================
class Solution:
    def add1(self, digits):
        if not digits:
            return []
        digits = [str(i) for i in digits]
        number = "".join(digits)
        number = int(number)
        number += 1
        return [int(x) for x in str(number)]



s = Solution()
res = s.add1([1, 2, 3])
print(res)