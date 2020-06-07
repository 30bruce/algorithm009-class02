# coding: utf-8
# Created at 2020-06-07 


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []
        m = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
        }
        res = ['']
        for i in digits:
            res = [x + y for x in res for y in m[i]]
        return res

