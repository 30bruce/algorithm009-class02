# coding: utf-8
# Created at 2020-06-07 


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        p, q分列左右子树，那么root即是最近公共祖先
        p == root 的情况，p即是最近公共祖先；
        q == root 的情况，q即是最近公共祖先
        """
        if not root or p == root or q == root:
            return root

        leftNode = self.lowestCommonAncestor(root.left, p, q)
        rightNode = self.lowestCommonAncestor(root.right, p, q)

        if not leftNode:
            return rightNode
        if not rightNode:
            return leftNode

        return root



