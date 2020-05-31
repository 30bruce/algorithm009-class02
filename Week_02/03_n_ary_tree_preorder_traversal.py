# coding: utf-8
# Created at 2020-05-31 


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.children:
            return [root.val]

        res = [root.val]
        for childNode in root.children:
            res += self.preorder(childNode)
        return res



