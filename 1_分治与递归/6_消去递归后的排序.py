# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 6_消去递归后的排序.py
# @Time       ：2024/1/4 20:26
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================

def merge(sub1, sub2):
    result = []
    i = j = 0
    while i < len(sub1) and j < len(sub2):
        if sub1[i] <= sub2[j]:
            result.append(sub1[i])
            i += 1
        else:
            result.append(sub2[j])
            j += 1
    result.extend(sub1[i:])
    result.extend(sub2[j:])
    return result



def merge_sort(arr):
    # 将arr添加到stack中
    stack = []
    for i in range(len(arr)):
        stack.append([arr[i]])

    while len(stack) > 1:
        sub1_stack = stack.pop()
        sub2_stack = stack.pop()

        sub_merge = merge(sub1_stack, sub2_stack)
        stack.append(sub_merge)
    return stack[0]

arr = [6, 8, 1, 5, 9, 3, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)
























