# coding: utf-8
# Created at 2020-06-07 


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return nums

        res = []
        self.helper(nums, [], res)
        return res

    def helper(self, nums, pre, res):
        if not nums:
            return res.append(pre[:])

        for i, v in enumerate(nums):
            self.helper(nums[:i]+nums[i+1:], pre+[nums[i]], res)



