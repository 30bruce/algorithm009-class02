# -*- coding: utf-8 -*-
# Created at 2020-07-19 


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([w[::-1] for w in s.split(' ')])


