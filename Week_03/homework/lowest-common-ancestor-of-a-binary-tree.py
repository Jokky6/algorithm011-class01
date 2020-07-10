#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   lowest-common-ancestor-of-a-binary-tree.py    
@Contact :   13801489449@163.com
@License :   (C)Copyright 2019-2020,林间有风

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/10 1:27 下午   Jokky      1.0         None
'''
"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
"""

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if not root:return root
#         if root.val == p.val or root.val == q.val:return root
#         left = self.lowestCommonAncestor(root.left,p,q)
#         right = self.lowestCommonAncestor(root.right,p,q)
#         if left and right:return root
#         if left:return left
#         if right:return right

class Solution:
    def lowestCommonAncestor(self,root:'TreeNode',p:'TreeNode',q: 'TreeNode') -> 'TreeNode':
        # If looking for me, return myself
        if root == p or root == q:
            return root

        left = right = None
        # else look in left and right child
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        # if both children returned a node, means
        # both p and q found so parent is LCA
        if left and right:
            return root
        else:
            # either one of the chidren returned a node, meaning either p or q found on left or right branch.
            # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
            # somewhere below node where 'p' was found we dont need to search all the way,
            # because in such scenarios, node where 'p' found is LCA
            return left or right
