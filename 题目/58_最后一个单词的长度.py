# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 58_最后一个单词的长度.py
# @Time       ：2023/12/11 19:25
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。



示例 1：

输入：s = "Hello World"
输出：5
解释：最后一个单词是“World”，长度为5。
示例 2：

输入：s = "   fly me   to   the moon  "
输出：4
解释：最后一个单词是“moon”，长度为4。
示例 3：

输入：s = "luffy is still joyboy"
输出：6
解释：最后一个单词是长度为6的“joyboy”。
"""
# ================【功能：】====================
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip()
        str_list = s.split(' ')
        return len(str_list[-1])


s = Solution()
intervals = [[1, 5]]
newInterval = [2, 3]
res = s.lengthOfLastWord("   fly me   to   the moon  ")
print(res)

