# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 106_从中序与后序遍历序列构造二叉树.py
# @Time       ：2024/3/26 19:50
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
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

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        for i in range(len(postorder)):
            self.valToIndex[inorder[i]] = i
        return self.build(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

    def build(self, inorder, inStart, inEnd, postorder, postStart, postEnd):
        if inStart > inEnd:
            return None

        rootval = postorder[postEnd]
        root = TreeNode(rootval)
        index = self.valToIndex.get(rootval)
        leftsize = index - inStart
        root.left = self.build(inorder, inStart, index - 1,
                               postorder, postStart, postStart + leftsize - 1)
        root.right = self.build(inorder, index + 1, inEnd,
                               postorder, postStart + leftsize, postEnd - 1)
        return root





# leetcode submit region end(Prohibit modification and deletion)
