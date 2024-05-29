# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 50_POW.py
# @Time       ：2023/12/4 19:15
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ）。
示例 1：

输入：x = 2.00000, n = 10
输出：1024.00000
示例 2：

输入：x = 2.10000, n = 3
输出：9.26100
示例 3：

输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25

"""
# ================【功能：】====================


class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = x
        if n > 0:
            for i in range(1, n):
                res *= x
        elif n < 0:
            for i in range(1, -n):
                res *= x
            res = 1 / res
        else:
            return 1
        return res


s = Solution()
matrix = [""]
res = s.myPow(2, -2)
print(res)