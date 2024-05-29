# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 罗马转整数.py
# @Time       ：2023/9/21 19:23
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class Solution:
    def intToRoman(self, s: str) -> int:
        roman_to_int = [('M', 1000), ('CM', 900), ('D', 500),
                        ('CD', 400), ('C', 100), ('XC', 90),
                        ('L', 50), ('XL', 40), ('X', 10),
                        ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]
        res = 0
        for i, j in roman_to_int:
            while s.startswith(i):
                res += j
                print(s)
                s = s.removeprefix(i)
        return res


if __name__ == '__main__':
    s = Solution()
    x_list = 'III'
    res = s.intToRoman(x_list)
    print(res)