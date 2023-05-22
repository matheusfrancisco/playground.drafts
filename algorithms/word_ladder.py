from typing import List
import collections

class Solution:
    # https://leetcode.com/problems/word-ladder/
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nbr = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nbr[pattern].append(word)

        visited = set([beginWord])
        q = collections.deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nbr_word in nbr[pattern]:
                        if nbr_word not in visited:
                            visited.add(nbr_word)
                            q.append(nbr_word)
            res += 1
        return 0
