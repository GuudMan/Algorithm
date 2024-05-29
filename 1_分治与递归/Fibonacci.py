# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : Fibonacci.py
# @Time       ：2024/1/2 19:36
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
def fibonacci(num):
    if num == 1:
        return 1
    if num == 2:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

res = fibonacci(3)
print(res)