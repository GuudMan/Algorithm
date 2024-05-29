# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 回文数.py
# @Time       ：2023/9/18 19:13
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
例如，121 是回文，而 123 不是。


示例 1：
输入：x = 121
输出：true

示例 2：
输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3：
输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数
"""
# ================【功能：】====================
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x is None:
            return False
        x_old = list(str(x))
        x_list = list(str(x))
        x_list.reverse()

        if x_list == x_old:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    x = 123
    res = s.isPalindrome(x)
    print(res)