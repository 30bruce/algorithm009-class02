# -*- coding: utf-8 -*-
# Created at 2020-06-28 


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 0
        dp = [0]*len(s)
        for i, c in enumerate(s[1:], 1):
            if c == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                elif i - dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':  # 累加
                    dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if i-dp[i-1] >= 2 else 0) + 2

                res = max(res, dp[i])
        return res


