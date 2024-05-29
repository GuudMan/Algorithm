# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 20_有效的括号.py
# @Time       ：2024/3/19 19:08
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个只包括'('，')'，'{'，'}'，'['，']' 的字符串s，判断字符串是否有效。

有效字符串需满足：

1、 左括号必须用相同类型的右括号闭合。

2、 左括号必须以正确的顺序闭合。

示例 1：

输入：s = "([)]"
输出：false
示例 2：

输入：s = "()[]{}"
输出：true
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                left.append(c)
            else:  # 右括号  peek返回栈顶元素并不删除它
                if len(left) > 0 and self.leftOf(c) == left[-1]:
                    left.pop()
                else:  # 和最近的左括号不匹配
                    return False
        return len(left) <= 0

    def leftOf(self, c):
        if c == "}":
            return '{'
        if c == ")":
            return "("
        return "["

# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
res = s.isValid("()")
print(res)

