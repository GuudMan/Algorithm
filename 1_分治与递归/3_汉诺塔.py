# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 3_汉诺塔.py
# @Time       ：2024/1/4 18:41
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================

def hanoi(n, a, b, c):
   if n == 1:
       print(a, "->", c)
   else:
       hanoi(n - 1, a, c, b)
       hanoi(1, a, b, c)
       hanoi(n - 1, b, a, c)
hanoi(5, 'a', 'b', 'c')








