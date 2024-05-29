# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 87_扰乱字符串.py
# @Time       ：2023/12/26 19:23
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isScramble(self, s1: str, s2: str):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n, m = len(s1), len(s2)
        if n != m or list(s1).sort() != list(s2).sort():
            return False
        if n < 4 and s1 == s2:
            return True
        f = self.isScramble
        for i in range(1, n):
            if (f(s1[:i], s2[:i]) and f(s1[i:], s2[i:])) or (f(s1[i:], s2[:-i]) and f(s1[:i], s2[-i:])):
                return True
        return False


s = Solution()
res = s.isScramble("great", "rgeat")
print(res)
