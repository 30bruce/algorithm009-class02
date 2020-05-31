# coding: utf-8
# Created at 2020-05-31


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = {}
        for i, num in enumerate(nums):
            delta = target - num
            if delta in numDict:
                return [numDict[delta], i]
            numDict[num] = i

        return []
