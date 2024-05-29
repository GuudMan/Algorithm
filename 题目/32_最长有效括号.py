# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 32_最长有效括号.py
# @Time       ：2023/11/7 19:22
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        # dp[i] 的定义：记录以 s[i-1] 结尾的最长合法括号子串长度
        dp = [0] * (len(s) + 1)
        print(dp)
        for i in range(len(s)):
            if s[i] == '(':
                # 遇到左括号，记录索引
                stk.append(i)
                # 左括号不可能是合法括号子串的结尾
                dp[i + 1] = 0
            else:
                # 遇到右括号
                if stk:
                    # 配对的左括号对应索引
                    leftIndex = stk.pop()
                    print(leftIndex)
                    # 以这个右括号结尾的最长子串长度
                    length = 1 + i - leftIndex + dp[leftIndex]
                    dp[i + 1] = length
                    print(dp)
                else:
                    # 没有配对的左括号
                    dp[i + 1] = 0
        # 计算最长子串的长度
        res = 0
        for i in range(len(dp)):
            res = max(res, dp[i])
        return res


s = Solution()
output = s.longestValidParentheses("()(()(")
print(output)