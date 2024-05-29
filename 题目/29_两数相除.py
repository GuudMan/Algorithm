# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 29_两数相除.py
# @Time       ：2023/11/6 19:00
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你两个整数，被除数 dividend 和除数 divisor。将两数相除，要求 不使用 乘法、除法和取余运算。

整数除法应该向零截断，也就是截去（truncate）其小数部分。例如，8.345 将被截断为 8 ，-2.7335 将被截断至 -2 。

返回被除数 dividend 除以除数 divisor 得到的 商 。

注意：假设我们的环境只能存储 32 位 有符号整数，其数值范围是 [−231,  231 − 1] 。
本题中，如果商 严格大于 231 − 1 ，则返回 231 − 1 ；如果商 严格小于 -231 ，则返回 -231 。



示例 1:

输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = 3.33333.. ，向零截断后得到 3 。
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = -2.33333.. ，向零截断后得到 -2 。
"""


# ================【功能：】====================
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # -231 <= dividend, divisor <= 231 - 1
        # return int(dividend / divisor)
        res = int(dividend / divisor)
        if res > 2 ** 31 - 1:
            res = 2 ** 31 - 1
        if res < -2 ** 31:
            return -2 ** 31
        return res


s = Solution()

output = s.divide(-2147483648, -1)
print(output)
