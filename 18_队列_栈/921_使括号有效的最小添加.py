# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 921_使括号有效的最小添加.py
# @Time       ：2024/3/19 18:59
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
输入一个括号字符串，返回使其成为合法括号串所需添加的最少括号数。

示例 1：
输入："())"
输出：1
解释：添加 1 个左括号成为 (())

示例 2：
   输入："((("
   输出：3
   解释：添加 3 个左括号成为 ()()()
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 记录插入次数
        res = 0
        # need变量记录右括号的需求量
        need = 0

        for i in range(len(s)):
            if s[i] == '(':
                # 对右括号的需求+1
                need += 1

            if s[i] == ')':
                # 对右括号的需求-1
                need -= 1

                if need == -1:
                    need = 0
                    # 需插入一个左括号
                    res += 1
        return res + need

s = Solution()

res = s.minAddToMakeValid("(")
print(res)























# leetcode submit region end(Prohibit modification and deletion)
