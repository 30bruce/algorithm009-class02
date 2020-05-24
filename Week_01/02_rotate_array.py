# coding: utf-8
# Created at 2020-05-24 


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        step = k % len(nums)
        if step != 0:
            nums[:step], nums[step:] = nums[-step:], nums[:-step]