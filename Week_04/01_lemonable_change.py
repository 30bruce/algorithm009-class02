# -*- coding: utf-8 -*-
# Created at 2020-06-11 


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five, ten = 0, 0  # 最开始只有5元，10元的数量
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                if five <= 0:   # 此时没有5元零钱
                    return False
                ten += 1
                five -= 1  # 找5元
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif ten <=0 and five >= 3:
                    five -= 3
                else:
                    return False

        return True


