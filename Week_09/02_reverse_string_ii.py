# -*- coding: utf-8 -*-
# Created at 2020-07-19 


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ""
        for i in range(0, len(s), 2 * k):
            res += (''.join(reversed(s[i:i + k])) + s[i + k: i + 2 * k])

        return res


