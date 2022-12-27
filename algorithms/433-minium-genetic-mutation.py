import collections
from typing import List

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        visit = set()

        q = collections.deque()
        q.append([start, 0])
        bank_gen = set(bank)
        g = {"A": ["C", "G", "T"], "C": ["A", "G", "T"], "G": ["A", "C", "T"], "T": ["A", "C", "G"]}

        def create_gen(s):
            possible = []

            for i in range(len(s)):
                letter = s[i]
                for n in g[letter]:
                    newg = s[:i] + n + s[i+1:]
                    if newg in bank_gen and newg not in visit:
                        possible.append(newg)
            return possible

        while q:
            s, changes = q.popleft()
            if s == end:
                return changes
            for next_gen in create_gen(s):
                if next_gen not in visit:
                    visit.add(next_gen)
                    q.append([next_gen, changes + 1])
        return -1
