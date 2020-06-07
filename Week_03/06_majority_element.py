# coding: utf-8
# Created at 2020-06-07 


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len(nums)
        tmp_map = {}
        for i in nums:
            tmp_map[i] = tmp_map.get(i, 0) + 1
            if tmp_map[i] > total / 2:
                return i
