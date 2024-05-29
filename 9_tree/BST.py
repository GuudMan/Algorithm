# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : BST.py
# @Time       ：2024/2/22 10:24
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
class TreeNode():
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.val)

class BST():
    def __init__(self, node=None):
        """

        :param node: 根节点
        """
        node = TreeNode(node)
        self.root_node = node

    def insert(self, x):
        """
        二叉树插入操作
        :param x:
        :return:
        """
        if self.is_exist(x): # 判断是否存在该节点
            return
        p = TreeNode(x)
        if self.root_node == None: # 如果树为空的话， 则将插入的节点置为根节点
            self.root_node = p
        else:
            cur = self.root_node
            pre = None
            while cur != None:  # 利用非递归的方法遍历
                pre = cur
                if cur.val < x:
                    cur = cur.right
                else:
                    cur = cur.left

            p.parent = pre
            if pre.val < x:
                pre.right = p
            else:
                pre.left = p

    def is_exist(self, k):
        cur = self.root_node
        while cur != None and cur.val != k:
            if k < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return True if cur != None else False


    def preorder_tree_walk(self, n):
        """
        先序遍历树节点
        :param n:
        :return:
        """
        if n != None:
            print(n.val, end=' ')
            self.preorder_tree_walk(n.left)
            self.preorder_tree_walk(n.right)

    def inorder_tree_walk(self, n):
        """
        中序遍历
        :param n:
        :return:
        """
        if n != None:
            self.inorder_tree_walk(n.left)
            print(n.val, end=' ')
            self.inorder_tree_walk(n.right)


    def postorder_tree_walk(self, n):
        """
        中序遍历
        :param n:
        :return:
        """
        if n != None:
            self.postorder_tree_walk(n.left)
            self.postorder_tree_walk(n.right)
            print(n.val, end=' ')


    def find_node(self, k):
        # 找到值为k的节点并返回
        cur = self.root_node
        while cur != None and cur.val != k:
            if k < cur.left:
                cur = cur.left
            else:
                cur = cur.right
        return cur


if __name__ == '__main__':
    bs_tree = BST(16)  # 初始化二叉树
    # 插入
    bs_tree.insert(9)
    bs_tree.insert(24)
    bs_tree.insert(12)
    bs_tree.insert(6)
    bs_tree.insert(20)
    bs_tree.insert(30)
    bs_tree.find_node(6)








