# -*- coding: utf-8 -*-
# Created at 2020-06-26 


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        def dp_max(arr, v):
            ans = float('-inf')
            for si, siv in enumerate(arr):
                tmp = 0
                for sj in range(si, len(arr)):
                    tmp += arr[sj]
                    if ans < tmp <= v:
                        ans = tmp
                        if ans == v:
                            return v
            return ans

        def dp_max_opt(arr, v):
            cur_sum = arr[0]
            max_sum = cur_sum
            for si, siv in enumerate(arr[1:]):
                if cur_sum > 0:
                    cur_sum += siv
                else:
                    cur_sum = siv

                max_sum = max(max_sum, cur_sum)

            if max_sum <= v:
                return max_sum

            # 再走一遍暴力，解决这种情况[1, 2, -9, 15] 7
            return dp_max(arr, v)

        res = float('-inf')
        row_len, col_len = len(matrix), len(matrix[0])
        for i in range(col_len):    # 左边界
            rowsSum = [0]*row_len
            for j in range(i, col_len):  # 右边界
                for i1 in range(row_len):
                    rowsSum[i1] += matrix[i1][j]

                res = max(res, dp_max_opt(rowsSum, k))
                if res == k:
                    return k
        return res







