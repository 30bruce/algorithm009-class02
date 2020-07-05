# -*- coding: utf-8 -*-
# Created at 2020-07-05 


class UnionFind(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def union(self, p, i, j):
        p1 = self.find(p, i)
        p2 = self.find(p, j)
        if p1 != p2:
            self.count -= 1
        p[p1] = p2

    @staticmethod
    def find(p, i):
        root = i
        while p[root] != root:
            root = p[root]

        while p[i] != i:
            i, p[i] = p[i], root

        return root


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(len(M))
        for i in range(len(M)):
            for j in range(i):
                if M[i][j] == 1:
                    uf.union(uf.parent, i, j)
        return uf.count



