# -*- coding: utf-8 -*-
# Created at 2020-06-14 

from collections import defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        begin_len = len(beginWord)  # 因为所有的的单词长度是一样的
        all_combo_dict = defaultdict(list)  # 所有单词变化一位后的所有单词映射 -> {'*ot': ['hot', 'dot', 'lot'], 'h*t': ['hot'], ...}
        for word in wordList:
            for i in range(begin_len):
                all_combo_dict["{}*{}".format(word[:i], word[i+1:])].append(word)

        queue = [(beginWord, 1)]
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)
            for i in range(begin_len):
                # 单词在all_combo_dict中的 key 串
                key = "{}*{}".format(current_word[:i], current_word[i+1:])
                for word in all_combo_dict[key]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level+1))

                all_combo_dict[key] = []

        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

s = Solution()
s.ladderLength(beginWord, endWord, wordList)







