# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 104_二叉树的最大深度.py
# @Time       ：2024/3/23 14:58
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数，叶子节点是指没有子节点的节点。

示例：
给定二叉树[3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#  1. 回溯法
# class Solution(object):
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         self.res = 0
#         self.traverse(root, 0)
#         return self.res
#
#     # 遍历二叉树
#     def traverse(self, root, depth):
#         if not root:
#             return
#         # 前序遍历位置
#         depth += 1
#         # 遍历的过程中记录最大深度
#         self.res = max(self.res, depth)
#         self.traverse(root.left, depth)
#         self.traverse(root.right, depth)
#         # 后序遍历位置
#         depth -= 1

# leetcode submit region end(Prohibit modification and deletion)


# 2、 动态规划法
class Solution(object):
    def maxDepth(self, root):
        # 定义： 输入一个节点， 返回以该节点为根的二叉树的最大深度
        if not root:
            return 0
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        # 根据左右子树的最大深度推出原二叉树的最大深度
        return 1 + max(leftMax, rightMax)








