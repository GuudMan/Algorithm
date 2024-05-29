# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 49_字母异位词分组.py
# @Time       ：2023/12/4 18:40
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2:

输入: strs = [""]
输出: [[""]]
示例 3:

输入: strs = ["a"]
输出: [["a"]]

"""
# ================【功能：】====================
class Solution:
    def groupAnagrams(self, strs):
        if len(strs) <= 1:
            return [strs]
        res = []
        res_dict = {}
        for i in range(len(strs)):
            str_i = ''.join(sorted(strs[i]))
            if str_i not in res_dict.keys():
                res_dict[str_i] = [i]
            else:
                values = res_dict.get(str_i)
                values.append(i)
                res_dict[str_i] = values

        for values_i in res_dict.values():
            res_i = []
            for i in values_i:
                res_i.append(strs[i])
            res.append(res_i)
        return res










s = Solution()
matrix = [""]
res = s.groupAnagrams(matrix)
print(res)




