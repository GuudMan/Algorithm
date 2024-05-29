# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 105_从前序与中序中构造二叉树.py
# @Time       ：2024/3/23 15:15
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
给定一棵树的前序遍历结果 preorder与中序遍历结果inorder，请构造二叉树并返回其根节点。
"""
# ================【功能：】====================

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def __init__(self):
        self.valToIndex = {}

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        for i in range(len(preorder)):
            self.valToIndex[inorder[i]] = i
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def build(self, preOrder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd:
            return None
        rootIndex = preOrder[preStart]
        root = TreeNode(rootIndex)

        index = self.valToIndex.get(rootIndex)
        leftsize = index - inStart

        # 构造左子树
        root.left = self.build(preOrder, preStart + 1, preStart + leftsize,
                               inorder, inStart, index - 1)
        root.right = self.build(preOrder, preStart + leftsize + 1, preEnd,
                               inorder, index + 1, inEnd)
        return root

# leetcode submit region end(Prohibit modification and deletion)
