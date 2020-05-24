# coding:utf-8


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        n = len(height)
        stack = []
        res = 0
        for i in range(n):
            #print(stack)
            while stack and height[stack[-1]] < height[i]:
                tmp = stack.pop()
                if not stack: break
                res += (min(height[i], height[stack[-1]]) - height[tmp]) * (i-stack[-1] - 1)
            stack.append(i)
        return res



