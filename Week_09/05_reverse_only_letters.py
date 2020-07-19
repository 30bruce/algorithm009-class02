# -*- coding: utf-8 -*-
# Created at 2020-07-19 


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        non_chars = []
        char_arr = []
        for i, c in enumerate(S):
            c_int = ord(c)
            if ord('a') <= c_int <= ord('z') or ord('A') <= c_int <= ord('Z'):
                char_arr.append(c)
            else:
                non_chars.append((i, c))

        char_arr.reverse()
        for i, c in non_chars:
            char_arr.insert(i, c)

        return ''.join(char_arr)


