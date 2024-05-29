# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 整数反转.py
# @Time       ：2023/9/13 3:54
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

示例 1：
输入：x = 123
输出：321

示例 2：
输入：x = -123
输出：-321

示例 3：
输入：x = 120
输出：21

示例 4：
输入：x = 0
输出：0

"""
# ================【功能：】====================
class Solution:
    def reverse(self, x: int) -> int:
        if x is None:
            return 0
        if x < 0:
            flag = True
        else:
            flag = False

        x = abs(x)
        x_list = list(str(x))
        x_list.reverse()

        reverse_x = ''.join(x_list)
        reverse_x = int(reverse_x)
        if reverse_x > 2**31 - 1:
            return 0
        elif reverse_x < -(2**31):
            return 0
        else:
            if flag:
                reverse_x = -reverse_x
            return reverse_x

if __name__ == '__main__':
    s = Solution()
    x = -0
    res = s.reverse(x)
    print(res)