# coding: utf-8
# Created at 2020-05-31 

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = [[root.val]]
        children = root.children
        while children:
            tmp = []
            tmp_children = []
            for node in children:
                tmp.append(node.val)
                if node.children:
                    tmp_children.extend(node.children)
            children = tmp_children
            res.append(tmp)

        return res
