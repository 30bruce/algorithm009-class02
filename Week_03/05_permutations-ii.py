# coding: utf-8
# Created at 2020-06-07 


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        track = [0]*len(nums)
        self.helper([], nums, track, res)
        return res

    def helper(self, pre, nums, track, res):
        if len(pre) == len(nums):
            return res.append(pre)

        for i, v in enumerate(nums):
            if track[i] == 1:
                continue
            if i > 0 and v == nums[i-1] and track[i-1] == 0:
                continue
            track[i] = 1
            self.helper(pre+[v], nums, track, res)
            track[i] = 0



