# -*- coding: utf-8 -*-
# Created at 2020-07-12 


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n != 0 and n & -n == n


