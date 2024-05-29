# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 超级素数幂.py
# @Time       ：2023/8/17 18:59
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：

如果一个数字能表示成 p^q，且p是一个素数，q为大于1的正整数，则此数字就是超级素数幂。
param number: 测试该数字是否是超级素数幂
return: 如果不是就返回 False，如果是就返回 p 和 q 值
例如，输入125，返回（5，3）
"""
# ================【功能：】====================
import math

def find_zhishu(i):
    for j in range(2, i):
        if i % j == 0:
            return 2
    return i

def num_sushu(num):
    # 先将数开根号
    scope = int(math.sqrt(num))
    zhishu = set()
    # 在scope范围内找素数
    for i in range(2, scope + 1):
        zhishu.add(find_zhishu(i))
    zhishu = list(zhishu)

    print(zhishu)
    res = []
    for p in zhishu:
        q = 2
        while p ** q <= num:
            if p ** q == num:
                res.append((p, q))
            q += 1
    return res


if __name__ == '__main__':
    num = 17*17
    res = num_sushu(num)
    print(res)
