"""
Problem Statement#
You are visiting a farm to collect fruits. The farm has a single row of fruit trees.
You will be given two baskets, and your goal is to pick as many fruits as possible
to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree.
The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
You can start with any tree, but you can’t skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5

Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

complexity O(N+N) = O(N)
space O(1)

similar problems
longest substring with at most 2 distinct characters
"""

def solution(fruits):
    start = 0
    max_lenght = 0
    bask = {}
    for end in range(len(fruits)):
        f = fruits[end]
        if f not in bask:
            bask[f] = 0
        bask[f] += 1

        while len(bask) > 2:
            ff = fruits[start]
            bask[ff] -= 1
            if bask[ff] == 0:
                del bask[ff]
            start += 1
        max_lenght = max(max_lenght, end - start + 1)
    return max_lenght


assert 3 == solution(['A', 'B', 'C', 'A', 'C'])
