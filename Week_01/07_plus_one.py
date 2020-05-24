# coding: utf-8
# Created at 2020-05-24 


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = True
        for i, v in enumerate(digits[::-1]):
            if v < 9:
                digits[len(digits)-i-1] = v+1
                flag = False
            else:
                digits[len(digits) - i - 1] = 0
            if not flag:
                break
        else:
            digits = [1] + digits
        return digits