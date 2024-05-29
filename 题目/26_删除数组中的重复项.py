# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 26_删除数组中的重复项.py
# @Time       ：2023/10/31 19:08
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
删除有序数组中的重复项
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，
使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。
然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：

更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，
并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。
判题标准:

系统会用下面的代码来测试你的题解:
输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素

输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。

"""
# ================【功能：】====================

class Solution:
    def removeDuplicates(self, nums):
        # if len(nums) < 1:
        #     return 0
        # slow, fast = 0, 0
        # while fast < len(nums):
        #     if nums[slow] != nums[fast]:
        #         slow += 1
        #         nums[slow] = nums[fast]
        #     fast += 1
        # return slow + 1

        if len(nums) < 1:
            return 0
        new_list = []
        for i in nums:
            if i not in new_list:
                new_list.append(i)
        # return len(new_list)
        return new_list


s = Solution()
input = [1, 1, 2]
output = s.removeDuplicates(input)
print(output)






