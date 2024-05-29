# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 2_XPath.py
# @Time       ：2024/3/6 9:40
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
import urllib
from urllib import request
data_jd = request.urlopen("https://baidu.com").read().decode("utf-8", "ignore")
print(len(data_jd))















