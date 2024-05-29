# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 最长公共前缀.py
# @Time       ：2023/9/21 19:40
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

提示：
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成
"""
# ================【功能：】====================
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        else:
            strs = zip(*strs)
            res = ""
            for tmp in strs:
                if len(set(tmp)) == 1:
                    res += tmp[0]
                else:
                    break
        return res






if __name__ == '__main__':
    s = Solution()
    # x_list = ["dog","racecar","car"]
    # x_list = ["flower","flow","flight"]
    # x_list = ["flower","flower","flower","flower"]
    x_list = ["ab", "a"]
    # x_list = ['flower']
    res = s.longestCommonPrefix(x_list)
    print(res)