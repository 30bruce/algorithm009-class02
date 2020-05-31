# coding: utf-8
# Created at 2020-05-31 


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        import collections
        nums_counter = collections.Counter(nums)
        return heapq.nlargest(k, nums_counter.keys(), key=nums_counter.get)
