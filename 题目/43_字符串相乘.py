# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 43_字符串相乘.py
# @Time       ：2023/11/16 19:16
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。

示例 1:
输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
"""
# ================【功能：】====================
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


s = Solution()  # 1 1 2 5 6 7 10
output = s.multiply("12", "345")
print(output)