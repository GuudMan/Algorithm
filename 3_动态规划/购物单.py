# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 购物单.py
# @Time       ：2024/1/25 9:28
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：

输入描述：
输入的第 1 行，为两个正整数N，m，用一个空格隔开：
（其中 N （ N<32000 ）表示总钱数， m （m <60 ）为可购买的物品的个数。）


从第 2 行到第 m+1 行，第 j 行给出了编号为 j-1 的物品的基本数据，每行有 3 个非负整数 v p q

（其中 v 表示该物品的价格（ v<10000 ），
 p 表示该物品的重要度（ 1 ~ 5 ），
  q 表示该物品是主件还是附件。如果 q=0 ，表示该物品为主件，
  如果 q>0 ，表示该物品为附件， q 是所属主件的编号）


输出描述：
 输出一个正整数，为张强可以获得的最大的满意度。
示例1
输入：
1000 5
800 2 0
400 5 1
300 5 1
400 3 0
500 2 0
输出：
2200

示例2
输入：
50 5
20 3 5
20 3 5
10 3 0
10 2 0
10 1 0
复制
输出：
130
复制
说明：
由第1行可知总钱数N为50以及希望购买的物品个数m为5；
第2和第3行的q为5，说明它们都是编号为5的物品的附件；
第4~6行的q都为0，说明它们都是主件，它们的编号依次为3~5；
所以物品的价格与重要度乘积的总和的最大值为10*1+20*3+20*3=130

"""
# ================【功能：】====================
def package(n, w, v, p, q):
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if j - v[i-1] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - v[i - 1]] + v[i - 1] * p[i - 1])
    return dp[n][w]



n = 5
w = 50
v = [20, 20, 20, 10, 10]
p = [3, 3, 3, 2, 1]
q = [5, 5, 0, 0, 0]
res = package(n, w, v, p, q)
print(res)