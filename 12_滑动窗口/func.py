# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : func.py
# @Time       ：2024/2/28 10:03
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
from collections import Counter

s = Counter('abc')
t = Counter('bac')
print(s == t)