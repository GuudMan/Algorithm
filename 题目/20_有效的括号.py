# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 20_有效的括号.py
# @Time       ：2023/10/10 19:29
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

 输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成


"""
# ================【功能：】====================
class Solution:
    def isValid(self, s: str) -> bool:
        def leftof(str_c):
            if str_c == ")":
                return "("
            elif str_c == "]":
                return "["
            else:
                return "{"
        left = []
        for c in s:
            if c in ['(', "{", "["]:
                left.append(c)
            else:
                if left and leftof(c) == left[-1]:
                    left.pop()
                else:
                    return False
        return not left


if __name__ == '__main__':
    s = Solution()
    str_s = "["
    res = s.isValid(str_s)
    print(res)
