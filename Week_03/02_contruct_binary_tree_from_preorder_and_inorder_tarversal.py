# coding: utf-8
# Created at 2020-06-07 


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        # 前序遍历列表中第一个元素为当前子树的根节点
        root_val = preorder[0]
        root = TreeNode(root_val)
        # 因为没有重复元素，直接根据值来查找根节点在中序遍历中的位置
        root_index = inorder.index(root_val)
        # 在中序遍历中获取左子树元素
        i_left_tree = inorder[:root_index]
        # 在前序遍历中获取左子树元素（因为左子树元素个数相等）
        p_left_tree = preorder[1:1+root_index]
        # 构建左子树
        root.left = self.buildTree(p_left_tree, i_left_tree)

        # 在中序遍历中获取右子树元素
        i_right_tree = inorder[root_index+1:]
        # 在前序遍历中获取右子树元素
        p_right_tree = preorder[1+root_index:]
        # 构建右子树
        root.right = self.buildTree(p_right_tree, i_right_tree)
        return root
