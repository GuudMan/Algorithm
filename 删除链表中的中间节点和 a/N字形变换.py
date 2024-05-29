# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : N字形变换.py
# @Time       ：2023/9/11 19:51
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);
示例 1：
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

示例 3：
输入：s = "A", numRows = 1
输出："A"

"""
# ================【功能：】====================
class Solution:
    def ZTransformer(self, s: str, numRows) -> str:
        res = []
        len_s = len(s)
        if len_s <= 0:
            return ''
        arr_step = []
        arr_step.append(2 * (numRows - 1))
        for i in range(numRows):
            k = 0
            if i != numRows - 1:
                jn = 2 * (numRows - 1) - 2 * i
            else:
                jn = 2 * (numRows - 1)
            while i + k * jn < len_s:
                if i + k * jn < len_s:
                    res.append(s[i + k * jn])
                k += 1
        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    str1 = 'PAYPALISHIRING'
    res = s.ZTransformer(str1, 3)
    print(res)
