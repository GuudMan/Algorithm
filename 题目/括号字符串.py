# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 括号字符串.py
# @Time       ：2023/8/15 19:09
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
1、给定一个字符串，判断这个字符串是不是有效的括号字符串，也就是满足数学算式可算性。
比如，str=”(()(())())”,返回 True，给定str = “(()((())(())”，
返回False。如果括号字符串中掺杂了其它的字符，则返回False
2、给定一个括号字符串，找出其中最大的子串长度，
比如：给定str = “(()((())(())”，返回 8。
"""
# ================【功能：】====================
def brackets_is_valid_1(str):
    if len(str) <= 0:
        return False
    stack = []
    for i in range(len(str)):
        if str[i] != "(" and str[i] != ")":
            print('----')
            return False
        if str[i] == "(":
            stack.append("(")
        else:
            stack.pop()
    if stack:
        return False
    else:
        return True


def brackets_is_valid_2(str):
    if len(str) <= 0:
        return False
    num1 = 0
    num2 = 0
    for i in range(len(str)):
        if str[i] != "(" and str[i] != ")":
            print('----')
            return False
        if str[i] == "(":
            num1 += 1
        else:
            num2 += 1
            if num1 < num2:
                return False
    if num1 < num2:
        return False
    else:
        return True

def longest_sub_brackets(str):
    '''
    给定一个括号字符串 str，返回最长的有效括号字符串
    方法：动态规划求解，做到时间复杂度 o(n)，空间复杂度 o(n)。创建一个与字符串同等长度的数组 dp[]，
        其含义是对应 str[i]结尾的字符串的最长有效子串的长度。然后即可开始求解。
    :param str: 给定的括号字符串
    :return: 最长有效子串
    '''
    dp = []
    for _ in range(0, len(str)):
        dp.append(0)
    for i in range(0, len(str)):
        if str[i] == "(":
            dp[i] = 0
        if str[i] == ")":
            if i != 0:
                pre = i - dp[i - 1] - 1
                if str[pre] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[pre - 1]
    return max(dp)


if __name__ == '__main__':
    str = "()"
    res = brackets_is_valid_2(str)
    print(res)