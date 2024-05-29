# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 39_组合总和.py
# @Time       ：2023/11/13 19:40
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：

给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，
找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，
并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。

对于给定的输入，保证和为 target 的不同组合数少于 150 个。

示例 1：

输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
示例 2：

输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
示例 3：

输入: candidates = [2], target = 1
输出: []

"""
# ================【功能：】====================
class Solution:
    def __init__(self):
        self.res = []
    def combinationSum(self, candidates, target: int):
        candidates.sort()
        if not candidates:
            return self.res
        self.backtrack(candidates, 0, target, 0)
        return self.res

    # 记录回溯路径
    track = []

    # 回溯算法主函数
    def backtrack(self, candidates, start, target, sum):
        if sum == target:
            # 找到目标和
            if self.track[:] not in self.res:
                self.res.append(self.track[:])
            return
        if sum > target:
            # 超过目标和
            return

        # 回溯算法框架
        for i in range(start, len(candidates)):
            # 选择candicates[i]
            self.track.append(candidates[i])
            sum += candidates[i]
            # if sum > target:
                # self.backtrack(candidates, i + 1, target, sum)
            # 递归遍历下一层回溯树
            self.backtrack(candidates, i + 1, target, sum)
            # 撤掉选择  candidate[i]
            sum -= candidates[i]
            self.track.pop()


s = Solution()  # 1 1 2 5 6 7 10
output = s.combinationSum([10,1,2,7,6,1,5], 8)
print(output)