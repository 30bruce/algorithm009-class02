# coding: utf-8
# Created at 2020-05-24 


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = -1  # first zero index
        for i, v in enumerate(nums):
            if v == 0 and j <= -1:
                j = i
            elif v != 0 and j > -1:
                nums[i], nums[j] = 0, nums[i]
                j += 1