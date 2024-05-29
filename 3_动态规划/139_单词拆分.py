# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 139_单词拆分.py
# @Time       ：2024/1/22 17:23
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""
# ================【功能：】====================

class Solution():
    def wordBreak(self, s: str, wordDict):
        self.memo = [-1] * len(s)
        return self.dp(s, 0, wordDict)
    def dp(self, s, i, wordDict):
        if i == len(s):
            return True
        if self.memo[i] != -1:
            return True if self.memo[i] == 1 else False

        for word in wordDict:
            length = len(word)
            if i + length > len(s):
                continue

            pre_s = s[i: i + length]
            if pre_s != word:
                continue

            if self.dp(s, i + length, wordDict):
                self.memo[i] = 1
                return True
        self.memo[i] = 0
        return False


    # def wordBreak(self, s: str, wordDict) -> bool:
    #     # 备忘录，-1 代表未计算，0 代表 false，1 代表 true
    #     self.memo = [-1] * len(s)
    #
    #     # 根据函数定义，判断 s[0..] 是否能够被拼出
    #     return self.dp(s, 0, wordDict)
    #
    # # 定义：返回 s[i..] 是否能够被 wordDict 拼出
    # def dp(self, s: str, i: int, wordDict) -> bool:
    #     # base case，整个 s 都被拼出来了
    #     if i == len(s):
    #         return True
    #
    #     # 防止冗余计算
    #     if self.memo[i] != -1:
    #         return True if self.memo[i] == 1 else False
    #
    #     # 遍历所有单词，尝试匹配 s[i..] 的前缀
    #     for word in wordDict:
    #         length = len(word)
    #         if i + length > len(s):
    #             continue
    #         sub_str = s[i:i + length]
    #
    #         if sub_str != word:
    #             continue
    #
    #         # s[i..] 的前缀被匹配，去尝试匹配 s[i+len..]
    #         if self.dp(s, i + length, wordDict):
    #             # s[i..] 可以被拼出，将结果记入备忘录
    #             self.memo[i] = 1
    #             return True
    #
    #     # s[i..] 不能被拼出，结果记入备忘录
    #     self.memo[i] = 0
    #     return False


s = Solution()
res = s.wordBreak("cars", ["car", "ca", "rs"])
print(res)





