# coding: utf-8
# Created at 2020-05-31 


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res_map = {}
        for s in strs:
            sorted_s = ''.join(sorted(list(s)))
            if sorted_s in res_map:
                res_map[sorted_s].append(s)
            else:
                res_map[sorted_s] = [s]
        return res_map.values()

