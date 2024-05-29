# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 去掉字符中连续的k个0.py
# @Time       ：2023/7/18 19:51
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定字符串str 和一个整数k。如果str中恰好出现了连续的k个0，则将k个0删除。
比如，给定字符串str = “0000fw300001203h000ui0000re3_0000”，k=4。返回的结果为“fw31203h000uire3_”。
"""
# ================【功能：】====================
def k_zero(strs1, k):
    if strs1 == "":
        return False
    k_0 = '0' * k
    while k_0 in strs1:
        strs1 = strs1.replace(k_0, "")
    return strs1


if __name__ == '__main__':
    strs1 = "0000fw300000001203h000ui0000re3_0000---000"
    k = 4
    res = k_zero(strs1, k)
    print(res)