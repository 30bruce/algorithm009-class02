# -*- coding: utf-8 -*-
# Created at 2020-07-19 


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = {}
        for c in s:
            res[c] = res.get(c, 0) + 1

        for i, c in enumerate(s):
            if res[c] == 1:
                return i
        return -1
