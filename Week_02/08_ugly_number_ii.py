# coding: utf-8
# Created at 2020-05-31 


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1] * n   # 初始化结果列表
        a, b, c = 0, 0, 0  # 三个指针
        for i, v in enumerate(res[1:], 1):
            min_v = min([res[a]*2, res[b]*3, res[c]*5])
            if min_v == res[a]*2:
                a += 1
            if min_v == res[b]*3:
                b += 1
            if min_v == res[c]*5:
                c += 1

            res[i] = min_v

        return res[-1]


s = Solution()
print s.nthUglyNumber(10)


