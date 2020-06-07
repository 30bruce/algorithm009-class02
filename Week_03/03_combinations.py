# coding: utf-8
# Created at 2020-06-07 


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        # 从1开始，找到n
        self.helper(1, k, n, [], res)
        return res

    def helper(self, start, k, n, pre, res):
        if len(pre) == k:
            return res.append(pre[:])

        for i in range(start, n+1):
            pre.append(i)
            self.helper(i+1, k, n, pre, res)
            pre.pop()


s = Solution()
print s.combine(4, 1)

