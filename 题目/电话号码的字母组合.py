# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 电话号码的字母组合.py
# @Time       ：2023/9/26 19:42
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
输入：digits = ""
输出：[]

示例 3：
输入：digits = "2"
输出：["a","b","c"]
"""


# ================【功能：】====================
# class Solution(object):
    # def letterCombinations(self, digits):
    #     if digits == "":
    #         return []
    #     phone_dict = {'2': 'abc',
    #                   '3': 'def',
    #                   '4': 'ghi',
    #                   '5': 'jkl',
    #                   '6': 'mno',
    #                   '7': 'pqrs',
    #                   '8': 'tuv',
    #                   '9': 'wxyz',
    #                   }
    #     res = []  # 存放结果列表
    #     middle_res = []  # 存放中间结果列表
    #     lens = len(digits)  # 长度即middle_res中元素个数
    #     index = 0  # 回溯下标
    #
    #     def recall(index):
    #         if lens == index:
    #             res.append("".join(middle_res))
    #         else:
    #             for item in phone_dict[digits[index]]:
    #                 middle_res.append(item)
    #                 recall(index + 1)
    #                 middle_res.pop()
    #
    #     recall(index)
    #     return res
class Solution(object):
    # 每个数字到字母的映射
    mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def __init__(self):
        self.res = []

    def letterCombinations(self, digits: str):
        if not digits:
            return self.res
        # 从 digits[0] 开始进行回溯
        self.backtrack(digits, 0, [])
        return self.res

    # 回溯算法主函数
    def backtrack(self, digits: str, start: int, path):
        if len(path) == len(digits):
            # 到达回溯树底部
            self.res.append(''.join(path))
            return
        # 回溯算法框架
        for i in range(start, len(digits)):
            digit = int(digits[i])
            for c in self.mapping[digit]:
                # 做选择
                path.append(c)
                # 递归下一层回溯树
                self.backtrack(digits, i + 1, path)
                # 撤销选择
                path.pop()


if __name__ == '__main__':
    s = Solution()
    digits = "23"
    res = s.letterCombinations(digits)
    print(res)
