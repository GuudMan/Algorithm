# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : BinTree.py
# @Time       ：2024/2/22 10:00
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class TreeNode():
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right



class BinTree():
    def __init__(self):
        self.root = None  # 初始化根节点为None
        self.ls = []

    def add(self, data):
        node = TreeNode(data)
        if self.root == None:
            self.root = node
            self.ls.append(self.root)
        else:
            rootNode = self.ls[0]
            if rootNode.left == None:
                rootNode.left = node
                self.ls.append(rootNode.left)
            elif rootNode.right == None:
                rootNode.right = node
                self.ls.append(rootNode.right)
                self.ls.pop(0)
    def preOrderTraversal(self, root):
        if root == None:
            return
        print(root.data)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)


if __name__ == '__main__':
    tree = BinTree()
    for i in range(1, 11):
        tree.add(i)
    tree.preOrderTraversal(tree.root)















