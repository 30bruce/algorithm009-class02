# -*- coding: utf-8 -*-
# Created at 2020-06-13 


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row_num = len(grid)
        if row_num == 0:
            return 0

        column_num = len(grid[0])
        res = 0
        for r in range(row_num):
            for c in range(column_num):
                if grid[r][c] == "1":
                    res += 1
                    self.dfs(grid, r, c)

        return res

    def dfs(self, grid, r, c):
        grid[r][c] = 0
        row_num, column_num = len(grid), len(grid[0])
        for x, y in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):  # 四个方向查找
            if 0 <= x < row_num and 0 <= y < column_num and grid[x][y] == "1":
                self.dfs(grid, x, y)

