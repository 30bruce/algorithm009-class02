# -*- coding: utf-8 -*-
# Created at 2020-06-14 


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not g or not s:
            return 0

        # 从大到小排序
        g.sort(reverse=True)
        s.sort(reverse=True)
        gi, si, ret = 0, 0, 0

        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:  # 满足胃口，分配给他
                si += 1
                ret += 1
            gi += 1

        return ret


