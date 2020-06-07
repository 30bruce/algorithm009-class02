# coding: utf-8
# Created at 2020-06-07 


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        visited = [False] * n
        paths = []

        def backtrace(row, pt, mem1, mem2):
            if row == n:
                paths.append(pt)
            for col in range(n):
                if not visited[col] and (row+col not in mem1) and (row-col not in mem2):
                    visited[col] = True
                    backtrace(row + 1, pt+[col], mem1 | {row+col}, mem2 | {row-col})
                    # revert state
                    visited[col] = False

        backtrace(0, [], set(), set())
        ans = [["."*i + "Q" + "." *(n - i - 1) for i in path] for path in paths]
        return ans
