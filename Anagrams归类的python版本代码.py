# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : Anagrams归类的python版本代码.py
# @Time       ：2023/8/14 19:49
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给出一组字符串，返回其中所有的 Anagrams。
比如， 给出 [“eat”, “tea”, “tan”, “ate”, “nat”, “bat”]，
返回
[
[“ate”, “eat”,”tea”],
[“nat”,”tan”],
[“bat”]
]
所有字母不分大小写。
"""


# ================【功能：】====================

def anagrams(str_list):
    str_list_ori = str_list.copy()
    if len(str_list) <= 0:
        return False
    res = []
    res_index = []
    for i in range(len(str_list)):
        str_list[i] = ''.join(sorted(str_list[i].lower()))
    res_dict = {}
    res_dict_index = {}
    for j in range(len(str_list)):
        if str_list[j] in res_dict:
            res_dict[str_list[j]] += [str_list[j]]
            res_dict_index[str_list[j]] += [j]
        else:
            res_dict[str_list[j]] = [str_list[j]]
            res_dict_index[str_list[j]] = [j]
    for k in res_dict:
        tem = res_dict[k]
        res += [tem]
    for k in res_dict_index:
        tem = res_dict_index[k]
        res_index += [tem]
    ans = []
    for j in res_index:
        temp = []
        for ji in j:
            temp += [str_list_ori[ji]]
        ans += [temp]
    return ans


if __name__ == '__main__':
    str_list = ["eat", "tea", "Tan", "ate", "nat", "bat"]
    res = anagrams(str_list)
    print(res)

