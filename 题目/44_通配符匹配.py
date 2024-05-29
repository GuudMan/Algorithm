# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 44_通配符匹配.py
# @Time       ：2023/11/16 19:20
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：

"""
# ================【功能：】====================
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        # 将p中相邻的*去除， 以提升效率
        pp = self.remove_adj_star(p)
        m, n = len(s), len(pp)
        # 备忘录初始化为 -1
        memo = [[-1] * n for _ in range(m)]
        # 执行自顶向下带备忘录的动态规划
        return self.dp(s, 0, pp, 0, memo)



    def remove_adj_star(self, p:str):
        if not p:
            return ""
        pp = p[0]
        for i in range(1, len(p)):
            if p[i] == '*' and p[i - 1] == '*':
                continue
            pp += p[i]
        return pp

    # 判断 s[i..]是否能被p[j..]匹配
    def dp(self, s, i, p, j, memo):
        # base case
        if j == len(p) and i == len(s):
            return True
        if i == len(s):
            for k in range(j, len(p)):
                if p[k] != '*':
                    return False
                return True

            if j == len(p):
                return False

            if memo[i][j] != -1:
                return bool(memo[i][j])
            res = False

            if s[i] == p[j] or p[j] == '?':
                # s[i] 和 p[j]完成匹配
                res = self.dp(s, i + 1, p, j + 1, memo)
            elif p[j] == '*':
                # s[i]和p[j]不匹配， 但p[j]不是通配符*
                # 可以匹配0个或多个s中的字符
                # 只要有一种情况能够完成匹配即可
                res = self.dp(s, i + 1, p, j, memo) or self.dp(s, i, p, j + 1, memo)
            # 将s[i]和p[j]的匹配结果存储备忘录
            memo[i][j] = res

            return res












s = Solution()  # 1 1 2 5 6 7 10
output = s.isMatch("12", "345")
print(output)