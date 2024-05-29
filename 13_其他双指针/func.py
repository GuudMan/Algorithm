# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : func.py
# @Time       ：2024/3/4 19:06
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
res = {1:0, 2:1, 3:2}
res[2] = res.get(2, 0) + 1
print(res)