# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 5_合并排序.py
# @Time       ：2024/1/4 19:26
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================

def merge(a, b):
    # c = []
    # h = j = 0
    # while j < len(a) and h < len(b):
    #     if a[j] < b[h]:
    #         c.append(a[j])
    #         j += 1
    #     else:
    #         c.append(b[h])
    #         h += 1
    #
    # if j == len(a):
    #     for i in b[h:]:
    #         c.append(i)
    # else:
    #     for i in a[j:]:
    #         c.append(i)
    c = a + b
    c = sorted(c)
    return c

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)



if __name__ == '__main__':
    import random
    random.seed(2)
    arr = [random.randint(0, 100) for _ in range(10)]
    print("原始数据：", arr)
    arr_new = merge_sort(arr)
    print("归并排序后的结果:", arr_new)









