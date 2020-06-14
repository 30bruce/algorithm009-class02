# -*- coding: utf-8 -*-
# Created at 2020-06-14 


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if not prices:
            return profit

        pre = prices[0]
        for price in prices[1:]:
            if price > pre:
                profit += price - pre

            pre = price
        return profit





