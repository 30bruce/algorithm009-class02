# coding: utf-8
# Created at 2020-05-31 


class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        arr = [0] * 26
        for i, c in enumerate(s):
            arr[ord(c) - 97] += 1
            arr[ord(t[i]) - 97] -= 1
        for n in arr:
            if n != 0:
                return False

        return True

    def isAnagramForOneLoop(self, s, t):
        if len(s) != len(t):
            return False
        c_map = {}
        for i, c in enumerate(s):
            c_map[c] = c_map.get(c, 0) + 1
            c_map[t[i]] = c_map.get(t[i], 0) - 1
            if c_map[c] == 0:
                del c_map[c]
            if c_map.get(t[i]) == 0:
                del c_map[t[i]]
        return not c_map

    def isAnagramByArr(self, s, t):
        arr = [0] * 26
        for c in s:
            arr[ord(c) - 97] += 1
        for c in t:
            arr[ord(c) - 97] -= 1
        for n in arr:
            if n != 0:
                return False

        return True

    def isAnagramByDict(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t) :
            return False

        s_map = {}
        for c in s:
            s_map[c] = s_map.get(c, 0) + 1

        for c in t:
            s_map[c] = s_map.get(c, 0) - 1
            if s_map[c] < 0:
                return False
            elif s_map[c] == 0:
                del s_map[c]
        return not s_map

    def isAnagramBySort(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(list(s)) == sorted(list(t))



s = Solution()
s.isAnagram("a", "ab")