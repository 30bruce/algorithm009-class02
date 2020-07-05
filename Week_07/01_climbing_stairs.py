

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        states = [-1]*(n+1)

        def recur(m):
            if m == 0 or m == 1:
                return 1
            if states[m] == -1:
                states[m] = recur(m-1) + recur(m-2)
            return states[m]

        return recur(n)


