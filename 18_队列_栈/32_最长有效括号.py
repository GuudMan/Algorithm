# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 32_最长有效括号.py
# @Time       ：2024/3/18 18:54
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个只包含'(' 和')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：

输入：s = "(()(()()("
输出：4
解释：最长有效括号子串是 "()()"
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stk = []
        # dp[i]的定义: 记录以s[i-1]结尾的最长合法括号子串长度
        dp = [0] * (len(s) + 1)
        for i in range(len(s)):
            if s[i] == '(':
                # 遇到左括号， 记录索引
                stk.append(i)
                # 左括号不可能是合法括号子串的结尾
                dp[i + 1] = 0
            else:
                # 遇到右括号
                if stk:
                    # 配对的左括号对应索引
                    leftIndex = stk.pop()
                    # 以这个右括号结尾的最长子串长度
                    length = 1 + i - leftIndex + dp[leftIndex]
                    dp[i + 1] = length
                else:
                    # 没有配对的左括号
                    dp[i + 1] = 0
        # 计算最长子串的长度
        res = 0
        for i in range(len(dp)):
            res = max(res, dp[i])
        return res

# leetcode submit region end(Prohibit modification and deletion)
