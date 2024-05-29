# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 定长数组.py
# @Time       ：2023/8/30 15:45
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
定长数组，如果超过，就删除旧元素，保留最新的元素
"""
# ================【功能：】====================


class FixLengthList():
    def __init__(self, maxlength=5):
        self.maxlength = maxlength
        self.list = []

    def add(self,value):
        if len(self.list) == self.maxlength:
            self.list.pop(0)
            self.list.append(value)
        else:
            self.list.append(value)
    def get_list(self):
        return self.list

fix_list = FixLengthList(5)
fix_list.add(1)
fix_list.add(2)
fix_list.add(3)
fix_list.add(4)
fix_list.add(5)
print(fix_list.get_list())
fix_list.add(6)
print(fix_list.get_list())
